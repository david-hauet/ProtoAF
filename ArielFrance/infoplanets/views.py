from django.shortcuts import render
from .models import Exoplanet
import json
import requests

def getexoclockdata(request):

    allexoplanets = {}
    if request.GET.get('mybutton') == 'Click':
        url = 'https://www.exoclock.space/database/planets_json'
        exoclock_response = requests.get(url)
        serialized_exoclockdata = exoclock_response.json()
        

        for planet, planetdata in serialized_exoclockdata.items(): 
                exoplanet_API = Exoplanet(
                    name = planetdata['name'],
                    type = '',
                    priority = planetdata['priority'],
                    total_observations = planetdata['total_observations'],
                    recent_observations = planetdata ['recent_observations'],
                    ra_j2000 = planetdata['ra_j2000'],
                    dec_j2000 = planetdata['dec_j2000'],
                    v_mag = planetdata['v_mag'],
                    r_mag = planetdata['r_mag'],
                    gaia_g_mag = planetdata['gaia_g_mag'],
                    depth_mmag = planetdata['depth_mmag'],
                    transit_duration_hours = planetdata['duration_hours'],
                    ephemeris_mid_time_bjd_tdb = planetdata['t0_bjd_tdb'],
                    ephemeris_mid_time_uncertainty = planetdata['t0_unc'],
                    ephemeris_period_days = planetdata['period_days'],
                    ephemeris_period_uncertainty = planetdata['period_unc'],
                    ephemeris_current_oc_min = planetdata['current_oc_min']
                )

                if Exoplanet.objects.filter(name=exoplanet_API.name).exists(): 
                    continue
                else: 
                    exoplanet_API.save()

        allexoplanets = Exoplanet.objects.all().order_by('name')

    return render(request, 'infoplanets.html', {'exoplanets' : list(allexoplanets)})

def is_it_json(serialized_exoclockdata):
    try:
        json.loads(serialized_exoclockdata)
    except ValueError as nope:
        return False
    return True

def checker(request):
    jsonbooleanchecker = 'No info'
    if is_it_json == True:
        jsonbooleanchecker = 'JSON'
    if is_it_json == False: 
        jsonbooleanchecker = 'Not a JSON'

    return render(request, 'infoplanets.html', {'isitajson' : jsonbooleanchecker})

    




