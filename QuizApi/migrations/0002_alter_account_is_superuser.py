# Generated by Django 3.2.1 on 2024-05-17 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.CharField(max_length=6),
        ),
    ]
