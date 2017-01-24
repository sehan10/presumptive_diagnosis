from django.conf.urls import  url
from . import  views

urlpatterns =[

    url(r'^home', views.index, name='index'),
    #url(r'^UserForm/', views.naivebayes, name='naivebayes'),
    url(r'^Webapp/Submit', views.Submit, name='submit'),
    url(r'^aboutus' ,views.aboutus, name='aboutus' ),
    url(r'^contactus', views.contactus, name='contactus'),
    url(r'^home', views .home, name='home'),


]
