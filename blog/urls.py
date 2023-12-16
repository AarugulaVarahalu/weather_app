from django.urls import path

from .views import weather_app,todo_app,remove,user_logout,user_register,user_login,home,second_home,about
urlpatterns =[
    path('', home, name="index"),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('about/',about,name='about'),

    #app level
    path('second/',second_home,name='second'),
    path('weather_app/', weather_app, name='weather'),
    path('todo_app/', todo_app, name='todo'),
    path('del/<str:item_id>', remove, name="del"),
    path('index/', user_logout, name='logout')
]