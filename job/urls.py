from  django.urls import path

from . import views

indatacollection = [
    path('', views.index, name='index'),
    path('collection/', views.indatacollection, name='indatacollection'),
    path('data/', views.jobdata, name='jobdata'),
    path('result/', views.jobresult, name='jobresult')
]
urlpatterns = indatacollection
