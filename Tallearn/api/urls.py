from django.urls import path
from api.blog_n_events_api.views_bne_api import BlogPostApiView, CategoryPostApiView, EventApiView
from api.about_api.views_about_api import AboutApiView, ContactApiView

urlpatterns = [
    path('api/v1/categorypostlist', CategoryPostApiView.as_view()),
    path('api/v1/postlist/<int:category>', BlogPostApiView.as_view()),
    path('api/v1/eventlist', EventApiView.as_view()),

    path('api/v1/aboutlist', AboutApiView.as_view()),
    path('api/v1/contactlist', ContactApiView.as_view()),





]