from django.urls import path


from .import views

urlpatterns = [
   path('courses/', views.CategoryListView.as_view(), name='courses'),
   path('', views.home)
]