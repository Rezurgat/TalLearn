from django.urls import path

from api.blog_n_events_api.views_bne_api import BlogPostApiView, CategoryPostApiView, EventApiView

urlpatterns = [
    path('api/v1/blogpostlist', BlogPostApiView.as_view()),
    path('api/v1/categorypostlist', CategoryPostApiView.as_view()),
    path('api/v1/eventlist', EventApiView.as_view())




]