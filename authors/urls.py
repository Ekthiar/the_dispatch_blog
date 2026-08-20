from django.urls import path
from . import views

urlpatterns = [
    path('Registration/', views.registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('changePassword/',views.change_pass, name = 'change_pass')
]
