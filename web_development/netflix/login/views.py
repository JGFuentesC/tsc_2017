# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    path = "login/login.html"
    return render(request, path, {"boton-login": False, "ruta": "login"})
