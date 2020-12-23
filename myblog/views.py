from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Count
from myblog.models import *
# Create your views here.

def get_blog_list_common_data(request, post_all_list):
    page_num = request.GET.get('page', 1) #get url 頁面參數
    paginator = Paginator(post_all_list, 5) #每5篇文進行分頁
    page_of_posts = paginator.get_page(page_num)
    curr_page_num = page_of_posts.number #取現在頁碼
    #取現在頁碼前後兩頁的範圍
    page_range_display = list(range(max(curr_page_num -2,1), curr_page_num)) + \
    list(range(curr_page_num, min(curr_page_num + 2, paginator.num_pages) + 1))

    #前頁碼省略記號與後頁碼省略記號
    if page_range_display[0] - 1 >= 2:
        page_range_display.insert(0, "...")
    if paginator.num_pages - page_range_display[-1] >= 2:
        page_range_display.append('...')
    #第一頁與最後一頁
    if page_range_display[0] != 1:
        page_range_display.insert(0,1)
    if page_range_display[-1] != paginator.num_pages:
        page_range_display.append(paginator.num_pages)
        
    #Blog 分類數量
    # BlogPostCategory.objects.annotate(blog_post_count=Count('blog_post'))
    #Blog 分類 by日期
    blog_post_dates = BlogPost.objects.dates("created_at", "month", order="DESC")
    blog_post_date_dict = {}
    for blog_post_date in blog_post_dates:
        blog_count = BlogPost.objects.filter(created_at__year=blog_post_date.year
                                             ,created_at__month=blog_post_date.month).count()
        blog_post_date_dict[blog_post_date] = blog_count  
        
    context = {}
    context['posts'] = page_of_posts.object_list
    context['page_of_posts'] = page_of_posts
    context['page_range_display'] = page_range_display
    context['category_list'] = BlogPostCategory.objects.annotate(blog_post_count=Count('blogpost'))
    context['posts_date'] = blog_post_date_dict
    print(blog_post_date_dict)
    return context

class HomeView(View):
    template_name = 'myblog/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class PostListView(View):
    template_name = 'myblog/post_list.html'
    def get(self, request, *args, **kwargs):
        post_list = BlogPost.objects.all().order_by("-created_at")
        context = get_blog_list_common_data(request, post_list)
        return render(request, self.template_name, context)
    
class PostDetailView(View):
    template_name = 'myblog/post_detail.html'
    def get(self, request, pk):
        post = get_object_or_404(BlogPost, pk=pk)
        context = {}
        context['post'] = post
        context['previous_post'] = BlogPost.objects.filter(created_at__gt=post.created_at).last()
        context['next_post'] = BlogPost.objects.filter(created_at__lt = post.created_at).first()
        return render(request, self.template_name, context)
        
class PostCategoryView(View):
    template_name = 'myblog/post_category.html'
    def get(self, request, pk):
        category = get_object_or_404(BlogPostCategory, pk=pk) #取類別
        post_list = BlogPost.objects.filter(category=category) #通過類別篩選需要的文章
        context = get_blog_list_common_data(request, post_list)
        context['post_by_categories'] = category
        return render(request, self.template_name, context)
    
class PostDateView(View):
    template_name = 'myblog/post_category_date.html'
    def get(self, request,yyyy, mm):
        post_list = BlogPost.objects.filter(created_at__year=yyyy, created_at__month=mm) #哪一年月的post
        context = get_blog_list_common_data(request, post_list)
        context['posts_with_date'] = f"{yyyy}/{mm}"
        context['posts_list'] =post_list
        return render(request, self.template_name, context)
# class PostListView(ListView):
#     model = BlogPost
#     template_name = 'myblog/post_list.html'
#     context_object_name = "post_list"
    # queryset = BlogPost.objects.all()
    
    # def get(self,request):
    #     posts = BlogPost.objects.all()
    #     return render(request, self.template_name)

    # def get_queryset(self):
    #     return BlogPost.objects.filter().order_by('created_at')

class AboutView(View):
    def get(self, request):
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
        <h1> Leonard's Blog </h1>
        <hr>
        <p> I am Leonard Tseng. Oh Ya!</p>
        <table width=400 border=1 bgcolor="#ccffcc">
        {}
        </table>
        </body>
        </html>
        """
        blog_post = BlogPost.objects.all()
        tags = f"""
        <tr>
            <td>標題</td>
            <td>摘要</td>
            <td>類別</td>
            <td>標籤</td>
            <td>作者</td>
        </tr>"""
        for b in blog_post:
            tags = tags + f"<tr><td>{b.title}</td>"
            tags = tags + f"<td>{b.summary}</td>"
            tags = tags + f"<td>{b.get_category()}</td>"
            tags = tags + f"<td>{b.show_tags()}</td>"
            tags = tags + f"<td>{b.author}</td></tr>"
        return HttpResponse(html.format(tags))
    
class DogView(View):
    template_name = 'dog.html'
    def get(self, request):
        return render(request, self.template_name, {})
        # html = f"<h3>dog num:{yyyy}/{dd}/{mm}/{dog_no} ya ya ya!</h3><hr>"

# class DogView(View):
#     template_name = 'dog.html'
#     def get(self, request):
#         yyyy = "2013"
#         mm = "10"
#         dd = "20"
#         dog_no = "02"
#         html = f"<a href='{}'>dog yayaya</a>" \ 
#             .format(reverse('post-url', args = (yyyy,mm,dd,dog_no)))
#         return HttpResponse(html)
