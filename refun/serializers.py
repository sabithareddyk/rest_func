from rest_framework.serializers import ModelSerializer

from refun.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
