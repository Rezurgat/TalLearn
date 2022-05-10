from django.urls import path

from .import views

urlpatterns = [
   path('blog_category/', views.CategoryListView.as_view(), name='category_list'),
   path('blog_category/<slug:slug>/', views.PostListView.as_view(), name='post_list'),
   path('events/', views.EventListView.as_view(), name='event_list')

]