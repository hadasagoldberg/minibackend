from django.shortcuts import render

# Create your views here.
from CommonUtils.views import redis_instance
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def prueba(request):
    if request.method == "GET":
        values = redis_instance.smembers('24.1.135861')
        print(values)
        return Response(values, status=200)