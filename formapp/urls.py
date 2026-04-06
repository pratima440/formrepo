from django.urls import path
from django.contrib import admin
from . import views
urlpatterns=[
    path('',views.show),
    path('add/',views.add_employee),
    path('show/',views.show_employee),

    path('edit/<int:id>/',views.edit_employee),
    path('update/<int:id>/',views.update_employee),
    path('delete/<int:id>/',views.delete_employee),
]
