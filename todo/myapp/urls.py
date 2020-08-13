from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('add_to_do', views.add_to_do, name='add_to_do'),
    path('delete/<int:todo_id>/', views.delete, name='delete')
]