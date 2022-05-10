from django.urls import path

from .import views

urlpatterns = [
   path('blog_category/', views.CategoryListView.as_view(), name='category_list'),
   path('events/', views.EventListView.as_view(), name='event_list')

]