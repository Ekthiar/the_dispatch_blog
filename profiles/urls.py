from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit_profile1', views.edit_profile1, name='editprofile1'),
    path('edit_profile2', views.edit_profile2, name='editprofile2'),
    path('deshboard/', views.dashboard, name='dashboard'),
]
