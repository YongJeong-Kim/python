from django.contrib import admin

# Register your models here.
from myapp.models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
