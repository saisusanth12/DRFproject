from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Student
from core.serializers import StudentSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'id_number': 25
        }
        return Response(data)
    
        

