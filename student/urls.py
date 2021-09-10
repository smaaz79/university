from django.urls import path
from . import views

urlpatterns = [
    path('add_student', views.add_student),
    path('adding_student', views.adding_student)
    path('view_student', views.view_student)
]
