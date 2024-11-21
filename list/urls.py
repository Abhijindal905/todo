from django.urls import path
from .views import *
urlpatterns = [
    path('',home_page,name='home'),
    path('login/',login_page,name='login'),

    path('register/',register_page,name='register'),
    path('index/', index_page,name='index'),
    path('delete-task/<str:name>', delete_task,name='delete'),
    path('update-task/<str:name>',update_task, name='update'),
    path('logout/', logoutview, name='logout')
]
