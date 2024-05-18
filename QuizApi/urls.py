from django.urls import path
from .views import manageaccount, manage_questions

urlpatterns = [
    path('accounts/', manageaccount, name='manage-account-list'),
    path('accounts/<int:pk>/', manageaccount, name='manage-account-detail'),

    path('questions/', manage_questions, name='manage_questions'),
    path('questions/<int:pk>/', manage_questions, name='manage_single_question'),
]
