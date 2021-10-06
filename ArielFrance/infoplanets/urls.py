from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('exoclockjson/', views.getexoclockdata),
    path('exoclockjson/', views.is_it_json)
]