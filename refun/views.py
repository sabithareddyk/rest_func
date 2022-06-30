from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from refun.models import Employee
from refun.serializers import EmployeeSerializer

# Create your views here.
@api_view(['GET','POST'])
def emp_list_or_create(request):
    if request.method == 'GET':
        emp_qs = Employee.objects.all()
        emp_serlializers = EmployeeSerializer(emp_qs, many=True)
        return Response(emp_serlializers.data, status=status.HTTP_200_OK)
    else:
        emp_serlializers = EmployeeSerializer(data = request.data)
        emp_serlializers.is_valid(raise_exception=True)
        emp_serlializers.save()
        return Response(emp_serlializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def emp_get_or_update(request, pk):
    emp = get_object_or_404(Employee, id=pk)
    if request.method == "GET":
        emp_serializers = EmployeeSerializer(emp)
        return Response(emp_serializers.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        emp_serializers = EmployeeSerializer(instance=emp, data=request.data)
        emp_serializers.is_valid(raise_exception=True)
        emp_serializers.save()
        return Response(emp_serializers.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        emp.delete()
        return Response({'msg': 'record deleted'}, status=status.HTTP_204_NO_CONTENT)


def home(request):
    return HttpResponse("hello u r in my site")