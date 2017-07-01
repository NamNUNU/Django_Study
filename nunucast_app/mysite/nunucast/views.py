# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .forms import CreateUserForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm
from django.template import loader, Context
from django.views.generic import View
    
# Create your views here.



class IndexView(TemplateView):
    template_name = 'nunucast/index.html'

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'


    