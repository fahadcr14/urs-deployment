from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('about', views.about, name ='about'), #It works like this first we have the name of the file we want to go to then its name
    #path('contact', views.register, name ='register'),  #To add user authentication first add a new URL named register
    # path('login', views.login, name ='login'),
    path('logout', views.logout, name ='logout'),
    path('getyourdestination', views.getyourdestination, name ='getyourdestination'),
    path('newaccountform', views.newaccountform, name ='newaccountform'),
    path('contact', views.contact, name ='contact'),
    path('form', views.form, name ='form'),
    path('post/<str:pk>', views.post, name ='post'), # We are using a string varible named pk i.e we can get a string here in dynamic URL EX: http://127.0.0.1:8000/post/jim
    #path('post/<int:pk>', views.post, name ='post') # We are using a int varible named pk i.e we can get a int here in dynamic URL EX: http://127.0.0.1:8000/post/12
]