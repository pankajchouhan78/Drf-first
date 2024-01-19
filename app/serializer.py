# the process of converting complex data such as querysets and model instances to native python datatypes are called serialization.
# a serializer class is very similar to a django form and modelform class.
# python se json or json se python

# complex datatype  --> serialization -- python native datatype --> render into json -- json data


from rest_framework import serializers
from .models import Course
class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    auther = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    discount = serializers.IntegerField(default=0)
