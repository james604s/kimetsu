


class BlogCommonDataUtilties:
    def get_post_list_common_data(self, posts_all_list):
        paginator = Paginator(post_list, 5) #每5篇文進行分頁
        page_num = request.GET.get('page', 1) #get url 頁面參數
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
        context = {}
        context['posts'] = page_of_posts.object_list
        context['page_of_posts'] = page_of_posts
        context['page_range_display'] = page_range_display
        context['category_list'] = BlogPostCategory.objects.all()
        context['posts_date'] = BlogPost.objects.dates('created_at', 'month', order="DESC")
    