from django.urls import path


from .import views

urlpatterns = [
   path('category/', views.CategoryListView.as_view(), name='category_list'),
   path('category/<slug:slug>/', views.CourseListView.as_view(), name='course_list'),
   path('', views.home)
]