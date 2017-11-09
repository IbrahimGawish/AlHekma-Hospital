from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^/result',views.result,name='result'),
    url(r'^/mobileApp',views.mobileApp,name='mobileApp'),

]