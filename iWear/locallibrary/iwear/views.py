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

from .forms import UserForm, MemInfoForm, PostForm
from .models import Accessories, Meminform, Style, Post, Follow, AuthUser, Friends

# Create your views here.
def homepage(request):
  own_posts = Post.objects.filter(userid = request.user)
  post = Post.objects.all()
  sql = """
  select post.userid, post.photo, post.time from follow, post where follow.memFoid = post.userid order by post.time desc
  """
  follows = Follow.objects.filter(userid = request.user)
  if follows: #追蹤好友貼文
    follow_posts = SelectAllSqlByColumns(sql, ['userid', 'photo', 'time'])
    posts = list(follow_posts) #按時間順序排(越新越上面)

  if request.method == 'get':
      pk=request.GET.get('search', '')
      mems = Meminform.objects.get(userid=pk)
      return render(request, 'iwear/profile_test.html', {'mems':mems})

  # else: #自己貼文
  #   posts = own_posts.order_by('-time') 

  return render(request, 'iwear/home.html', locals())


#setting.html
@login_required
def profile(request):
    mems = Meminform.objects.filter(userid=request.user).all()
    posts = Post.objects.filter(userid=request.user).order_by('-time') #貼文
    times = Post.objects.filter(userid=request.user).count() #發文數
    follows = Follow.objects.filter(userid=request.user).count() #追蹤數
    fans = Follow.objects.filter(memfoid__userid=request.user).count() #被追蹤數
    return render(request, 'iwear/profile.html', locals())

#Follows_profile
def profile_test(request, pk):
    mems = Meminform.objects.get(userid=pk)
    meminfos = Meminform.objects.filter(userid=pk).all()
    times = Post.objects.filter(userid=pk).count() #發文數
    posts = Post.objects.filter(userid=pk).order_by('-time') #貼文

    # if request.method == 'get':
    #   pk=request.GET.get('search', '')
    #   mems = Meminform.objects.get(userid=pk)
    
    return render(request, 'iwear/profile_test.html', locals())

#DB_FOLLOW
@login_required
def follow(request):
    follows = Follow.objects.filter(userid = request.user).all()  #__
    return render(request, 'iwear/follow.html', locals())

#FAN
@login_required
def friend(request):
#     friends = Friends.objects.filter(memno=request.user.id)
    return render(request, 'iwear/friend.html', locals())

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

#RECORD
@login_required
def record(request):
    template = get_template('iwear/record.html')
    html = template.render(locals())
    return HttpResponse(html)

#SEARCH
@login_required
def search(request):
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