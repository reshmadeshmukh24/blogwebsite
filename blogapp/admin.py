from django.contrib import admin
from blogapp.models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display=['title']


    prepopulated_fields={'slug':('title',)}


admin.site.register(Blog,BlogAdmin)