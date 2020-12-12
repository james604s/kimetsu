from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class BlogPostCategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = "blog_post_category"


class BlogPostTag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = "blog_post_tag"

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    summary = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(BlogPostCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField(BlogPostTag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def show_tags(self):
        return ",".join([t.name for t in self.tags.all()])

    def get_category(self):
        return self.category.name

    def __str__(self):
        return f"<Blog: {self.title}>"
    
    class Meta:
        managed = True
        db_table = "blog_post"
        ordering = ['-created_at']
    