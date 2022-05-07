from django.urls import path


from .import views

urlpatterns = [
   path('about/', views.AboutListView.as_view(), name='about_list')

]