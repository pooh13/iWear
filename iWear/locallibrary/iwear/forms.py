from django import forms
from django.forms import widgets
from iwear import models
# from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from iwear.models import Meminform, Post, Style

# Create the form class.
# 使用者
class UserForm(forms.ModelForm):
    # username = forms.CharField(label='帳號')
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleanedData = self.cleaned_data
        password = cleanedData.get('password')
        password2 = cleanedData.get('password2')
        if password and password2 and password!=password2:
            raise forms.ValidationError('密碼不相符')
        return cleanedData

class DateInput(forms.DateInput):
    input_type = 'date'

class MemInfoForm(forms.ModelForm):
    class Meta():
        widgets = {
            'birth': DateInput(),
        }
        model = Meminform
        fields = ('name', 'gender', 'birth', 'height', 'weight', 'mempic',)


# post 文章
class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('photo', 'word', 'styleno', 'accessoriesno', 'clothesno', 'coatno', 'pantsno', 'shoesno',)                                                                               

