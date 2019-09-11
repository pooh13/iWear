from django.contrib import admin

# Register your models here.
from .models import Accessories, Meminform, Style, Post, Follow
# , Clothes, Coat, Pants, Shoes, Style, Meminform

admin.site.register(Accessories)

@admin.register(Meminform)
class Meminform(admin.ModelAdmin):
    list_display = ('user', 'mempic')
    
admin.site.register(Style)

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('account', 'photo', 'time')

@admin.register(Follow)
class Follow(admin.ModelAdmin):
    list_display = ('id', 'memfono')

