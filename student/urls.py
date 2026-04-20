from django.urls import path
from .views import StudentListCreateAPIView, StudentDetailAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()), #List and Post
    path('students/<int:pk>/', StudentDetailAPIView.as_view()), #Update and Delete
]