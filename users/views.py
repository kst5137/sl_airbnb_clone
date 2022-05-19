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
from django.contrib.auth.hashers import check_password

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

@login_required
def user_delete(request):
    if request.method == 'POST':
        pw_del = request.POST["pw_del"]
        user = request.user

        if check_password(pw_del, user.password):
            user.delete()
            print('완료')
            return redirect('/')

    return render(request, 'users/delete.html')

@login_required
def change_password(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()

                return render(request, 'users/profile.html')
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})


    return render(request, 'users/changepassword.html',context)



def host_main(requeset):
    return render (requeset, 'airbnb/hostmain_test.html')