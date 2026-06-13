from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('departments/', views.departments),
    path('employees/', views.employees),
    path('add-department/',views.add_department),
    path('add-employee/',views.add_employee),
    
    path('edit-employee/<int:id>/',views.edit_employee),
    path('delete-employee/<int:id>/',views.delete_employee),
   
    path('edit-department/<int:id>/',views.edit_department),
    path('delete-department/<int:id>/',views.delete_department),
]
