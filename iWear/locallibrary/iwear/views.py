from django.shortcuts import render_to_response, HttpResponseRedirect, render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from django.urls import reverse
import datetime

from .forms import UserForm, MemInfoForm, PostForm
from .models import Accessories, Meminform, Style, Post
# , Clothes, Coat, Pants, Shoes, Style, Meminform


# Create your views here.
def homepage(request):
    template = get_template('iwear/homepage.html')
    html = template.render(locals())
    return HttpResponse(html)

#setting.html
@login_required
def setting(request):
    # mem = Meminform.objects.filter(user=request.user.id)
    mems = Meminform.objects.filter(user=request.user.id).all()
    posts = Post.objects.filter(account=request.user.id).order_by('-time')
    return render(request, 'iwear/setting.html', locals())

#addShow.html
# @login_required
# def addshow(request):
#   template = get_template('iwear/addShow.html')
#   html = template.render(locals())
#   return HttpResponse(html)

# post_create(addShow)
#addEdit.html
@login_required
def post_create(request):
  # style = Style.objects.all()
  if request.method == 'POST':
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      new_post = post_form.save(commit=False) # 保存數據，但暫時不提交到數據庫中
      new_post.account = request.user.id #指定account為使用者
      if 'photo' in request.FILES:
          new_post.photo = request.FILES['photo']
      new_post.save()
      return redirect('/')
    else:
      return render(request,'iwear/addEdit.html',{
        'post_form':post_form, 
      })
  else:
    post_form = PostForm()
    return render(request,'iwear/addEdit.html',{
      'post_form':post_form, 
  })



#addEdit.html
# @login_required
# def addedit(request):
#    template = get_template('iwear/addEdit.html')
#    html = template.render(locals())
#    return HttpResponse(html)   

#record.html
@login_required
def record(request):
    template = get_template('iwear/record.html')
    html = template.render(locals())
    return HttpResponse(html)

#search.html
@login_required
def search(request):
    template = get_template('iwear/search.html')
    html = template.render(locals())
    return HttpResponse(html)      

#Accessories
@login_required
def access(request):
    access = Accessories.objects.all()
    return render(request, 'test/accessInformation.html', {
        'access': access,
    })

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse(user.is_authenticated)
                # return HttpResponseRedirect(reverse('/'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})