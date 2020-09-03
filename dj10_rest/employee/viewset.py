from rest_framework import viewsets
from employee import models
from employee import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.Employee.objects.all()
    serializer_class=serializers.EmployeeSerializer
    