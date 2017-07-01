# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .forms import CreateUserForm
#from django.contrib.auth.forms import UserCreationForm
from django.template import loader, Context
from django.views.generic import View
    
# Create your views here.



class IndexView(TemplateView):
    template_name = 'nunucast/index.html'

class SignUpView(View):
    def post(self, request):
        form_class = CreateUserForm
        return HttpResponse(render(request, 'nunucast/signup.html', {"form":form_class}))


    