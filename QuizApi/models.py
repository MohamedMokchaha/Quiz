
from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_superuser = models.CharField(max_length=6)

    def __str__(self):
        return self.username


class Question(models.Model):
    category = models.CharField(max_length=100)
    question_text = models.CharField(max_length=500)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text