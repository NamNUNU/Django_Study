# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):
    lottos = GuessNumbers.objects.all();
    return render(request, "lotto/default.html", {"lottos":lottos})

def post(request):
    if request.method == "POST":
        #save data
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index')
    else :
        form = PostForm()
        return render(request, 'lotto/form.html', {"form":form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk = lottokey)
    return render(request, "lotto/detail.html", {"lotto": lotto})
