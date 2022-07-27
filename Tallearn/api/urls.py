from django.urls import path

from api.blog_n_events_api.views_bne_api import BlogPostApiView

urlpatterns = [
    path('api/v1/blogpostlist', BlogPostApiView.as_view()),




]