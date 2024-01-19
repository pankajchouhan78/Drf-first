from django.shortcuts import render

from .models import Course
from .serializer import CourseSerializer


from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from rest_framework.response import Response

# single model data
def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    print(course)
    serializer = CourseSerializer(course)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type = 'application/json') 

# multiple model data
def course_list(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    # many=True means bahoot sare objects hote hai 
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json') 
    return Response(serializer.data, safe=False)


# api banake use karna
# import requests
# Url = "http://127.0.0.1:8000/app/courses/"
# r = requests.get(url = Url)
# data = r.json()
# print(data)
