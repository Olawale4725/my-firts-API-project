# Generated by Django 4.1.7 on 2023-03-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phonenumber',
            field=models.CharField(max_length=15),
        ),
    ]
