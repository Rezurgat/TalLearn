from django.urls import path
from api.blog_n_events_api.views_bne_api import (
    PostListApiView,
    PostDetailApiView,
    CategoryPostListApiView,
    EventListApiView,
)
from api.about_api.views_about_api import AboutApiView, ContactApiView

urlpatterns = [
    path('api/v1/categorypostlist', CategoryPostListApiView.as_view()),
    path('api/v1/postlist/<int:category>', PostListApiView.as_view()),
    path('api/v1/postdetail/<int:pk>', PostDetailApiView.as_view()),
    path('api/v1/eventlist', EventListApiView.as_view()),

    path('api/v1/aboutlist', AboutApiView.as_view()),
    path('api/v1/contactlist', ContactApiView.as_view()),



]