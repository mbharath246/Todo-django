from django.urls import path
from todo import views

urlpatterns = [
    path('',views.dashboard, name="home"),
    path('add-task/',views.add_task, name="add"),
    path('delete-task/',views.delete_task, name="remove"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('search',views.search, name='search')
]