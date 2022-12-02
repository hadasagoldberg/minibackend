
# Create your views here.

from CommonUtils.views import redis_instance, separar_link
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

# searchstring - time - index - otypelist - maxresultsnum
@api_view(["GET"])
def search(request, **kwargs):
    if request.method == "GET":
        params = separar_link(str(kwargs["link"]))
        if len(params) == 5:
            values = eval(redis_instance.execute_command('INGRID.SEARCH', params[0], params[1], params[2], params[3], params[4]))
            print(values)
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# key - search - resultIni - resultsNum - sortby - order
@api_view(["GET"])
def ftsearch(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        if len(params) == 6:
            values = eval(redis_instance.execute_command('INGRID.FTSEARCH', params[0], params[1], params[2], params[3], params[4], params[5]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# network - lat - lon - rad - time
@api_view(["GET"])
def regen(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        if len(params) == 5:
            values = eval(redis_instance.execute_command('INGRID.REGEN', params[0], params[1], params[2], params[3], params[4]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# network - oid - time - computelist
@api_view(["GET"])
def regenarea(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        params[3] = params[3].replace('*','/')
        if len(params) == 4:
            values = eval(redis_instance.execute_command('INGRID.REGENAREA', params[0], params[1], params[2], params[3]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# update
@api_view(["GET"])
def update(request, **kwargs):
    if request.method == "GET":
        params = json.loads(request.body)
        #params = separar_link(kwargs["link"])
        if len(params) == 1:
            values = eval(redis_instance.execute_command('INGRID.UPDATE', params["changes"]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# oid - time - sourceList - networkList - excludedList - computelist
@api_view(["GET"])
def traverse(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        if len(params) == 6:
            values = eval(redis_instance.execute_command('INGRID.TRAVERSE', params[0], params[1], params[2], params[3], params[4], params[5]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# oid - time
@api_view(["GET"])
def oread(request, **kwargs):
    print("1")
    if request.method == "GET":
        print("2")
        params = separar_link(kwargs["link"])
        print("3")
        print("params", params)
        if len(params) == 2:
            values = eval(redis_instance.execute_command('INGRID.OREAD', params[0], params[1]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# oid - conceptName
@api_view(["GET"])
def val(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        if len(params) == 2:
            values = eval(redis_instance.execute_command('INGRID.VAL', params[0], params[1]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# companyoid - cfgtype - cfgname - cfgtime -cfgjson
@api_view(["GET"])
def updateconfig(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        if len(params) == 5:
            values = eval(redis_instance.execute_command('INGRID.UPDATECONFIG', params[0], params[1], params[2], params[3], params[4]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# companyid - gettime
@api_view(["GET"])
def getconfig(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        if len(params) == 2:
            true = True
            false = False
            values = eval(redis_instance.execute_command('INGRID.GETCONFIG', params[0], params[1]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)


# companyid - gettime
@api_view(["GET"])
def getconfigfo(request, **kwargs):
    if request.method == "GET":
        params = separar_link(kwargs["link"])
        if len(params) == 2:
            true = True
            false = False
            values = eval(redis_instance.execute_command('INGRID.GETCONFIGFO', params[0], params[1]))
            return Response(values, status=200)
        else:
            return Response("Faltan Parametros.", status=404)

