# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    path = "home/home.html"
    return render(request, path, {"boton_login": True, "ruta": "home"})
