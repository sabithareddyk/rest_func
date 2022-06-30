from django.contrib import admin
from django.urls import path, include
from refun.views import *

print("this is urls")
urlpatterns = [
       path('hi/', home),
       path('employee', emp_list_or_create, name="emp_list_or_create"),
       path('employee/<int:pk>/', emp_get_or_update, name="emp_get_or_update"),
]