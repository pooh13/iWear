from django.shortcuts import render_to_response, HttpResponseRedirect, render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from iwear.sqldata import SelectAllSqlByColumns
from itertools import chain
from operator import attrgetter
# from django.views import generic

from .forms import UserForm, MemInfoForm, PostForm, FollowForm
from .models import Accessories, Meminform, Style, Post, Follow, AuthUser, Friends, Postanalysisview

# Create your views here.
def homepage(request):
  own_posts = Post.objects.filter(userid = request.user)
  post = Post.objects.all()
  sql = """
  select post.userid, post.photo, style.style, post.word, post.time
  from follow, post, style
  where follow.memFoid = post.userid and post.styleNo = style.styleNo
  group by post.userid, post.photo, style.style, post.word, post.time
  order by post.time desc
  """
 
  if request.user: #追蹤好友貼文
    follow_posts = SelectAllSqlByColumns(sql, ['userid', 'photo', 'style', 'word', 'time'])
    posts = list(follow_posts) #按時間順序排(越新越上面)
  return render(request, 'iwear/home.html', locals())


#setting.html
@login_required
def profile(request):
    user = Meminform.objects.get(userid=request.user)
    mems = Meminform.objects.filter(userid=request.user).all()
    posts = Post.objects.filter(userid=request.user).order_by('-time') #貼文
    times = Post.objects.filter(userid=request.user).count() #發文數
    follows = Follow.objects.filter(userid=user).count() #追蹤數
    fans = Follow.objects.filter(memfoid=user).count() #被追蹤數
    return render(request, 'iwear/profile.html', locals())

#Follows_profile
def profile_test(request, pk): #pk=memfoid
    mems = Meminform.objects.get(userid=pk)
    meminfos = Meminform.objects.filter(userid=pk).all()
    times = Post.objects.filter(userid=pk).count() #發文數
    posts = Post.objects.filter(userid=pk).order_by('-time') #貼文

    user = Meminform.objects.get(userid=request.user)
    ##
    # 表-follow的userid是登入者 #登入者有追蹤memfoid
    if Follow.objects.filter(userid=user):
      if Follow.objects.filter(memfoid=pk):
        # 刪除追蹤好友
        if request.method == 'POST':
          follow_dic={}
          follow = request.POST
          follow_dic['userid'] = user
          follow_dic['memfoid'] = pk
          Follow.objects.filter(**follow_dic).delete()
      else:
        #新增追蹤好友
        if request.method == 'POST':
          memfoid = Meminform.objects.get(userid=pk)
          follow = Follow.objects.create(userid=user, memfoid=memfoid)
    #表-follow沒有userid是登入者
    else:
      #新增追蹤好友
      if request.method == 'POST':
        memfoid = Meminform.objects.get(userid=pk)
        follow = Follow.objects.create(userid=user, memfoid=memfoid)
    
    # 表-follow的userid是登入者 #登入者有追蹤memfoid
    if Follow.objects.filter(userid=user):
      if Follow.objects.filter(memfoid=pk):
        #btn顯示已追蹤
        follows = Follow.objects.all()
      else:
        #btn顯示追蹤
        unfollows = Meminform.objects.all()

    else:
      unfollows = Meminform.objects.all()

    return render(request, 'iwear/profile_test.html', locals())
    ##

    #搜尋
    # if 'search' in request.GET and request.GET['search']!='': #表單是否被提交
    #   pk = request.GET['search']

#DB_FOLLOW
@login_required
def follow(request):
    user = Meminform.objects.get(userid = request.user)
    follows = Follow.objects.filter(userid = user).all()  #__
    return render(request, 'iwear/follow.html', locals())

#FAN
@login_required
def fan(request):
    user = Meminform.objects.get(userid = request.user)
    fans = Follow.objects.filter(memfoid = user).all()
    return render(request, 'iwear/fan.html', locals())

#addEdit
@login_required
def post_create(request):
  if request.method == 'POST':
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      new_post = post_form.save(commit=False) # 保存數據，但暫時不提交到數據庫中
      if 'photo' in request.FILES:
          new_post.photo = request.FILES['photo']
      new_post.account = request.user.id
      new_post.userid = request.user
      new_post.save()
      return redirect('/')
    else:
      return render(request,'iwear/add_post.html',{
        'post_form':post_form, 
      })
  else:
    post_form = PostForm()
    return render(request,'iwear/add_post.html',{
      'post_form':post_form, 'time':datetime.now()
  })

#GROUP
@login_required
def group(request):
    template = get_template('iwear/group.html')
    html = template.render(locals())
    return HttpResponse(html)

#RECORD
@login_required
def record(request):
    template = get_template('iwear/record.html')
    html = template.render(locals())
    return HttpResponse(html)

#SEARCH
@login_required
def search(request):
    recommends = Postanalysisview.objects.filter(ownaccount=request.user.id)
    return render(request, 'iwear/search.html', locals())

#REGISTER
def register(request):
    # registered = False
    if request.method == 'POST':
      user_form = UserForm(request.POST)
      mem_form = MemInfoForm(request.POST, request.FILES)
      if user_form.is_valid() and mem_form.is_valid():
        user = user_form.save()
        user.set_password(user.password) 
        user.save()
        new_mem = mem_form.save(commit=False) # 暫存不存入資料庫, 因為mem.user不得為空值
        new_mem.user = user
        new_mem.userid = request.POST.get('username')
        if 'mempic' in request.FILES:
          new_mem.mempic = request.FILES['mempic']
        new_mem.save()
        # messages.success(request, '歡迎註冊')
        return redirect('/')
          # registered = True
      else:
        print(user_form.errors,mem_form.errors)
        return render(request,'registration/register.html',{
          'user_form':user_form, 
          'mem_form':mem_form, 
        })
    else:
      user_form = UserForm()
      mem_form = MemInfoForm()
      return render(request,'registration/register.html',{
        'user_form':user_form, 
        'mem_form':mem_form, 
        # 'registered':registered
      })

#LOGIN
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            #檢查該使用者是否有效
            if user.is_active:
                login(request,user)
                request.session['username']=username
                # return HttpResponseRedirect("/index")
                return HttpResponse(user.is_authenticated)
                # return HttpResponseRedirect(reverse('/'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})

#LOGOUT
@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))