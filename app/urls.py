
from django.urls import path
from . import views

urlpatterns = [
    path('courses/<int:pk>/', views.course_detail),
    path('courses/', views.course_list),
]
