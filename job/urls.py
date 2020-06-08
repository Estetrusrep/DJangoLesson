from  django.urls import path

from . import views

indatacollection = [
    path('', views.index, name='index'),
    path('collection/', views.indatacollection, name='indatacollection')
]
urlpatterns = indatacollection
