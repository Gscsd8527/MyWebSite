from django.urls import path
app_name = 'users'
from .views import Index, Login, Logout, Register, HotTopic, Recommend, UserData
urlpatterns = [
    path('', Index, name='index'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
    path('hot/', HotTopic, name='hot'),
    path('recommend/', Recommend, name='recommend'),
    path('userdata/', UserData, name='userdata'),
]