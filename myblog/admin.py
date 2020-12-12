#        return ",".join([t.tags for t in self.tags.all()])

from django.contrib import admin
from myblog.models import *

class BlogPostCategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    
class BlogPostTagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "summary", "get_category", "show_tags","author", "created_at", "updated_at"]

admin.site.register(BlogPostCategory, BlogPostCategoryAdmin)
admin.site.register(BlogPostTag, BlogPostTagAdmin)
admin.site.register(BlogPost, BlogPostAdmin)