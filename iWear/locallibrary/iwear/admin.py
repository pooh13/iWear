from django.contrib import admin

# Register your models here.
from .models import Accessories, Meminform, Style, Post, Follow, Friends, Clothes, Coat, Pants, Shoes, Postanalysisview

admin.site.register(Style)
admin.site.register(Accessories)
admin.site.register(Clothes)
admin.site.register(Coat)
admin.site.register(Pants)
admin.site.register(Shoes)
# admin.site.register(Postanalysisview)


@admin.register(Meminform)
class Meminform(admin.ModelAdmin):
    list_display = ('userid', 'mempic')

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('account', 'photo', 'time')

@admin.register(Follow)
class Follow(admin.ModelAdmin):
    list_display = ('userid', 'memfoid')

@admin.register(Friends)
class Friends(admin.ModelAdmin):
    list_display = ('memno', 'memfrno')

@admin.register(Postanalysisview)
class Meminform(admin.ModelAdmin):
    list_display = ('userid', 'photo')