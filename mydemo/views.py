from django.shortcuts import render
from django.views import View
from django.contrib import messages
# from django.core.paginator import Paginator

from mydemo.extractors import mask_data_extractors
# from mydemo.models import MaskData
from mydemo.plotly_charts import *
from mydemo.forms import MaskModelForm

def get_city_list_common_data(request, citydata_list):
    page_num = request.GET.get('page', 1) #get url 頁面參數
    paginator = Paginator(citydata_list, 8) #每5篇文進行分頁
    page_of_citydata = paginator.get_page(page_num)
    curr_page_num = page_of_citydata.number #取現在頁碼
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
    context['citydata'] = page_of_citydata.object_list
    context['page_of_citydata'] = page_of_citydata
    context['page_range_display'] = page_range_display
    # context['category_list'] = BlogPostCategory.objects.all()
    # context['posts_date'] = BlogPost.objects.dates('created_at', 'month', order="DESC")
    return context

# class MaskPlotlyView(TemplateView):
#     template_name = "mydemo/demo_mask2.html"
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(MaskPlotlyView, self).get_context_data(**kwargs)
#         context['plot_div'] = plot1d()
#         return context
class MaskPlotlyView(View):
    template_name = 'mydemo/demo_mask2.html'
    def get(self, request):
        # plot_div = plot1d()
        plot_div = test1()
        return render(request, self.template_name, context={"plot_div":plot_div})

    def post(self, request):
        form = MaskModelForm(request.POST)
        city = request.POST.get("city")
        action_type = request.POST.get("submit")
        return render(request, self.template_name, {"plot_div":plot_div})
    
def test11(request):
    # plot_div = plot1d()
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "mydemo/test11.html", context={'plot_div': plot_div})

def demo_mask1(request):
    if request.method == "POST":
        form = MaskModelForm(request.POST)
        if form.is_valid():
            city = request.POST.get("city")
            action_type = request.POST.get("submit")

            if action_type == "submit":
                ordering = request.POST.get("ordering")
                ordering = "-"+ordering
                mask_data_by_city = mask_data_extractors.get_mask_data_by_city(city, ordering)
                
                messages.success(request, (city + "剩餘口罩資訊"))
            elif action_type == "reset":
                messages.success(request, ("資料已清除"))
    else:
        form = MaskModelForm()
    return render(request, "mydemo/demo_mask1.html", locals()) 