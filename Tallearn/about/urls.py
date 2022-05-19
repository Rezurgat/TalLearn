from django.urls import path


from .import views

urlpatterns = [
   path('about/', views.AboutListView.as_view(), name='about_list'),
   path('contact/', views.ContactListView.as_view(), name='contact_list'),
   path('feedback/', views.CreateFeedback.as_view(), name='feedback'),


]