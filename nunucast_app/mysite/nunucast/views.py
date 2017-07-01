# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.template import loader, Context
from django.views.generic import View
from django.utils.decorators import method_decorator
    
# Create your views here.



class IndexView(TemplateView):
    template_name = 'nunucast/index.html'

class LoginView(View):
    def post(self, request):
        return HttpResponse("<h1>hello everyone</h1>")


    