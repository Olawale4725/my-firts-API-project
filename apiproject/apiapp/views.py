from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .sterilizer import StudentSerializer, StudenModelSerializers
from .models import Student
from rest_framework import status
from django.http import Http404

# Create your views here. 

class StudentList(APIView):
    def get(self, request, *args, **kwargs):
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        user_data=request.data
        serializer=StudenModelSerializers(data=user_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class StudentDetails(APIView):
    def get_object(self, pk):
        try:
            student=Student.objects.get(id=pk)
            return student 
        except Student.DoesNotExist:
            raise Http404

        
    def get(self, request, pk):
        student=self.get_object(pk)
        serializer = StudenModelSerializers(student)
        return Response (serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        Student=self.get_object(pk)
        serializer=StudentSerializer(Student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, pk):
        student=self.get_object(pk)
        student.delete()
        return Response({'message': 'student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

