import json

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view


from CommonUtils.views import redis_instance
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def prueba(request):
    if request.method == "GET":
        values = redis_instance.ping()
        print(values)
        return Response(values, status=200)


@api_view(["GET"])
def search(request, **kwargs):
    if request.method == "GET":

        values = redis_instance.execute_command('INGRID.SEARCH', str(kwargs["searchString"]),
                                                str(kwargs["time"]), str(kwargs["index"]),
                                                str(kwargs["oTypeList"]), str(kwargs["maxResultsNum"]))

        print(values)
        return Response(values, status=200)