from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginn,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.lout,name='lout'),
    path('',views.index,name ='index'),
    path('terms/',views.policy,name ='policy'),
]
