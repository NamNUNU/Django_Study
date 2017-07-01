# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.



def login(request):
    if request.method == "POST":
        return HttpResponse("<h1>hello everyone</h1>")

class IndexView(TemplateView):
    template_name = 'nunucast/index.html'


    