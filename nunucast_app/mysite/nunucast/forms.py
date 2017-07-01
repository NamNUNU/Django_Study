# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        #self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})

        for field in self.fields:
            self.fields[field].help_text=None
            self.fields[field].label=''
        
        self.fields['username'].widget.attrs['placeholder'] = "이름"
        self.fields['email'].widget.attrs['placeholder'] = "이메일"
        self.fields['password1'].widget.attrs['placeholder'] = "비밀번호"
        self.fields['password2'].widget.attrs['placeholder'] = "비밀번호 확인"


        