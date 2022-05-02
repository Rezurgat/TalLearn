from django.urls import path


from .import views

urlpatterns = [
   path('courses/', views.CategoryListView.as_view(), name='category_list'),
   path('', views.home)
]