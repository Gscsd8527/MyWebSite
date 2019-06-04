from django.urls import path
app_name = 'users'
from .views import Index, Login, Logout, Register
urlpatterns = [
    path('', Index, name='index'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
]