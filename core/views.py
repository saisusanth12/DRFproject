from django.shortcuts import render, HttpResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response

def post(self, request, *args, **kwargs):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


