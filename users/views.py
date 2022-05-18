from django.shortcuts import render

import json

from django.contrib import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
# from django.contrib.auth.models import User
from users.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import requests

# Create your views here.
def usermodify(requeset):
    return render (requeset, 'users/modify.html')
def host_main(requeset):
    return render (requeset, 'airbnb/hostmain_test.html')