from django.urls import URLPattern
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('complete/<slug:id>/',views.complete,name='completed'),
    path('delete/<slug:id>/',views.delete,name='delete'),
    path('logout/',views.logoutu,name='logout'),
    path('CompletedDelete/<int:id>/',views.completedelete,name='cdelete')
]