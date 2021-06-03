from django.urls import path
from myblog.views import *

urlpatterns = [
    # path('home/', HomeView.as_view()),
    path('', PostListView.as_view(), name='post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/category/<int:pk>', PostCategoryView.as_view(), name='post-category'),
    path('post/date/<int:yyyy>/<int:mm>',PostDateView.as_view(), name='post-category-date'),
    # path('post/', post_list),
    # path('about/', AboutView.as_view()),
    # path('dog/', DogView.as_view()),
    # path('dog/<int:yyyy>/<int:mm>/<int:dd>/<int:dog_no>', DogView.as_view(),name='post-url')

]