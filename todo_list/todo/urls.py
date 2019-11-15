from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_todo, name='add'),
    path('complete/<todo_id>', views.complete_todo, name='complete')
]
