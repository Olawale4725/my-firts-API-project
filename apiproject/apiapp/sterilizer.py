from rest_framework import serializers
from .models import Student



class StudenModelSerializers(serializers.ModelSerializer):
     class Meta:
          model=Student
          # fields=['id', 'firstname', 'lastname', 'gender', 'email', 'adress', 'phonenumber']
          fields='__all__'
          read_only_fields=['id']


class StudentSerializer(serializers.Serializer):
     GENDER_CHOICES=(
        ('Male', 'Male'),
        ('Female', 'female')
    )
     firstname=serializers.CharField(required=True, max_length=100)
     lastname=serializers.CharField(required=True, max_length=100)
     gender=serializers.ChoiceField(choices=GENDER_CHOICES)
     email=serializers.CharField(required=True, max_length=100)
     adress=serializers.CharField(required=True, max_length=100)
     phonenumber=serializers.CharField(required=True, max_length=100)


     def validate(self, attrs):
          return super().validate(attrs)
     
     def create(self, validated_data):
          student=Student.objects.create(**validated_data)
          return student
     
     def update(self, instance, validated_data):
          instance.firstname=validated_data.get('firstname', instance.firstname)
          instance.lastname=validated_data.get('lastname', instance.lastname)
          instance.gender=validated_data.get('gender', instance.gender)
          instance.email=validated_data.get('email', instance.email)
          instance.phonenumber=validated_data.get('phonenumber', instance.phonenumber)
          instance.adress=validated_data.get('adress', instance.adress)
          instance.save()
          return instance
     