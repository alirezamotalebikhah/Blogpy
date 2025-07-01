from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(UserProfile)
# admin.site.register(Category)
# admin.site.register(Article)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','avatar','description']
admin.site.register(UserProfile,UserProfileAdmin)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_at','category']
    search_fields = ['title','content']
admin.site.register(Article,ArticleAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','cover']
admin.site.register(Category,CategoryAdmin)