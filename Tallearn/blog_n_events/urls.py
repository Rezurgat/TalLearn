from django.urls import path

from .import views

urlpatterns = [

   path('blog/', views.CategoryListView.as_view(), name='blog_category_list'),
   path('blog/<slug:slug>/', views.PostListView.as_view(), name='post_list'),
   path('blog/<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_detail'),
   path('events/', views.EventListView.as_view(), name='event_list'),
   path('events/<slug:event_slug>/', views.EventDetailView.as_view(), name='event_detail'),

]