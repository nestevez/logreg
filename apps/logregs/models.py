# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt

# Create your models here.
class UsersManager(models.Manager):
    def users_valid(self, postData):
        errors = {}
        if postData['pw'] != postData['cpw']:
            errors['pw'] = 'Password and confirmation must match'
        if not re.match("^[A-Za-z]*$",postData['fname']):
            errors['fname'] = 'First name can only contain letters'
        if not re.match("^[A-Za-z]*$",postData['lname']):
            errors['lname'] = 'Last name can only contain letters'
        try:
            exists = Users.objects.get(email=postData['email'])
            errors['email'] = 'Email already taken! Try logging in'
        except Users.DoesNotExist:
            pass
        return errors

    def login_valid(self, postData):
        errors = {}
        err = False
        try:
            exists = Users.objects.get(email=postData['email'])
            safpw = exists.pw
            if not bcrypt.checkpw(postData['pw'].encode(), safpw.encode()):
                err = True
        except Users.DoesNotExist:
            err = True
        if err == True:
            errors['login']='The login information you have entered is incorrect'
        return errors

class Users(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    pw = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()
