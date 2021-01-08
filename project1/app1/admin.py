from django.contrib import admin
from app1.models import Post
from app1.models import Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):

	list_display = ['title', 'author', 'slug', 'body','publish', 'create', 'update', 'status']
	list_filter = ('status','author','create','publish',)
	search_fields = ('title','body',)
	prepopolated_fields = {'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):

	list_display = ['post', 'name','email', 'body', 'created', 'updated', 'active']
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')


admin.site.register(Comment, CommentAdmin)

admin.site.register(Post, PostAdmin)