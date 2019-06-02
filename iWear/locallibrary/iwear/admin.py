from django.contrib import admin

# Register your models here.
from .models import Accessories, Meminform, Style, Post
# , Clothes, Coat, Pants, Shoes, Style, Meminform

admin.site.register(Accessories)
# admin.site.register(Clothes)
# admin.site.register(Coat)
# admin.site.register(Pants)
# admin.site.register(Shoes)
# admin.site.register(Style)
# admin.site.register(Meminform)
@admin.register(Meminform)
class Meminform(admin.ModelAdmin):
    list_display = ('user', 'mempic')
admin.site.register(Style)
# admin.site.register(Post)
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('account', 'photo', 'time')

# admin.site.register(User)
# @admin.register(Meminform) 
# class Meminform(admin.ModelAdmin):
#     list_display = ('memno', 'account', 'name', 'gender', 'birth', 'mempic', 'height', 'weight')