from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from dex import views


urlpatterns = [
    path('', views.CuvantViewSet.as_view({'get': 'list'})),
    path('<cuvant_text>/', views.CuvantViewSet.as_view({'get': 'retrieve'})),
]
