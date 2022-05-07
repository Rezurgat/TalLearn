from django.urls import path


from .import views

urlpatterns = [
   path('category/comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
   path('category/', views.CategoryListView.as_view(), name='category_list'),
   path('category/<slug:slug>/', views.CourseListView.as_view(), name='course_list'),
   path('category/<slug:slug>/<slug:course_slug>/', views.CourseDetailView.as_view(), name='course_detail'),
   path('', views.home),
]