from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_category', views.add_category, name='add_category'),
    # path('savedata', views.savedata, name='savedata'),
    path('all_expense', views.all_expense, name='all_expense'),
   
]