from django.urls import path

from .import views

urlpatterns = [
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('events/', views.EventListView.as_view(), name='event_list')

]