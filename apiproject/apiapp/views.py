from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .sterilizer import StudentSerializer, StudentModelSerializers
from .models import Student
from rest_framework import status, generics
from django.http import Http404

# Create your views here. 
# class StudentListView(generics.ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentModelSerializers

class StudentListCreateView(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentModelSerializers

    def get_queryset(self):
        return self.queryset.filter(email__icontains="yahoo")

class GraduatingStudentView(generics.GenericAPIView):
    serializer_class=StudentModelSerializers
    queryset=Student.objects.all()

    def get(self, request, *args, **kwargs):
        qs=self.get_queryset().filter(email__icontains="gmail")
        serializer=self.serializer_class(qs, many=True)
        return Response({'message':'getting graduating student', "data":serializer.data}, status=status.HTTP_200_OK)
    

class StudentList(APIView):
    def get(self, request, *args, **kwargs):
        students=Student.objects.all()
        serializer=StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        user_data=request.data
        serializer=StudentModelSerializers(data=user_data)
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
        serializer = StudentModelSerializers(student)
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

