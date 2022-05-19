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
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from users.forms import SignupForm
from django.contrib import messages, auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm

# Create your views here.
# def userprofile(requeset):
#     return render (requeset, 'users/profile.html')
# # def user_modify(requeset):
#     # return render (requeset, 'users/modify.html')

def userprofile(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)


# @login_required
# def user_modify(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect('users/profile.html')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user)
#     return render(request, 'users/modify.html', {'user_form': user_form, 'profile_form': profile_form})
#

@login_required
def user_modify(request,pk):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # return redirect('/user/<int:pk>/')
        return render(request, 'users/profile.html')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
        'pk' : pk
    }
    print('fail')
    return render(request, 'users/modify.html', context)


def host_main(requeset):
    return render (requeset, 'airbnb/hostmain_test.html')