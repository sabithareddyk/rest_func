from django.contrib import admin

# Register your models here.
from refun.models import Employee

admin.site.register(Employee)
print("hi")