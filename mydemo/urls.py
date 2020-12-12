from django.urls import path
from mydemo.views import *

urlpatterns = [
    path('mask_charts/', MaskPlotlyView.as_view(), name='mask_charts'),
    path('test11/', test11, name='test11'),
    path('demo_mask1/', demo_mask1, name="demo_mask1")

]