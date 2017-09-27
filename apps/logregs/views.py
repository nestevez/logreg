# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .forms import Reg, Log
from .models import *
import bcrypt

# Create your views here.
def index(request):
    context = {
    'reg': Reg,
    'log': Log,
    }
    return render(request, 'logregs/index.html', context)

def register(request):
    reg = request.POST
    errors = Users.objects.users_valid(reg)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('home')
    else:
        pwhash = bcrypt.hashpw(reg['pw'].encode(), bcrypt.gensalt())
        Users.objects.create(fname=reg['fname'], lname=reg['lname'],email=reg['email'], pw=pwhash)
        request.session['user']=reg['fname']
        request.session['action']='registered'
        return redirect('success')

def login(request):
    log = request.POST
    errors = Users.objects.login_valid(log)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('home')
    else:
        request.session['user']=Users.objects.get(email=log['email']).fname
        request.session['action']='logged in'
        return redirect('success')

def success(request):
    context = {
    'action': request.session['action'],
    'user': request.session['user'],
    }
    return render(request, 'logregs/success.html', context)
