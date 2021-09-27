from django.shortcuts import render
from infoplanets.models import Exoplanet


def exoinfotest(request):

    queryset = Exoplanet.objects.get(pk=1)
    

# Create your views here.
