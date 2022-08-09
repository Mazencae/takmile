from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('details/<str:number>/<str:gender>',views.getDataSegnal),
    path('det/<str:gender>',views.getChois),
    #path('det/<str:pk>/create',views.createChois),
    path('det/<str:gender>/create',views.createChois,name='output_page'),
    path('update/<str:number>/<str:gender>',views.UpdateChois,name='update_page'),
    path('delete/<str:number>/<str:gender>',views.deleteChois,name='delete_page'),
    path('details/<str:gender>',views.getData),
    path('',views.getroot),
]