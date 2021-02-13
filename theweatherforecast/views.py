from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import finalTPred, finalWPred, finalPrecPred

def home_view(request):
    return render(request, 'mainpage.html', {'TempFrcst': finalTPred.showTempForecast, 'WindFrcst': finalWPred.showWindForecast, 'PrecpFrcst': finalPrecPred.showPrecpForecast})

def tomorrowsWeather(request):
    return render(request, 'tomorrow.html', {'TempFrcst': finalTPred.showTempForecast, 'WindFrcst': finalWPred.showWindForecast, 'PrecpFrcst': finalPrecPred.showPrecpForecast})
class  Frcst_List(APIView):
     def get(self, request, *args, **kw):
        get_arg1 = request.GET.get('arg1', None)
        get_arg2 = request.GET.get('arg2', None)
        get_arg3 = request.GET.get('arg3', None)
        myClass = finalTPred.showTempForecast(), finalWPred.showWindForecast(), finalPrecPred.showPrecpForecast()
        result = myClass
        response = Response(result, status=status.HTTP_200_OK)
        return response   