from django.contrib import admin
from django.urls import path, include
from django.views import View
from . import views

app_name ="ytproject"

urlpatterns = [
    path('',views.index, name='index'),
    path('download/',views.download,name ="download"),
    path('help/',views.help,name ="help"),
    path('support/',views.support,name ="support"),
    path('download/<str:resolution>/',views.download_done,name ="download_done"),
  
    # path('vdownload/<str:sid>/',views.vdownload,name ="vdownload")
]
