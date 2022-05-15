from django.urls import path


from .import views

urlpatterns = [
   path('about/', views.AboutListView.as_view(), name='about_list'),
   path('contact/', views.ContactView.as_view(), name='contact'),
   path('feedback/', views.CreateFeedback.as_view(), name='feedback'),


]