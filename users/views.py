import json
#
# from django.contrib import auth
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
# # from django.contrib.auth.models import User
# from users.models import User
# from django.db.models import Q
# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from django.shortcuts import render, redirect, get_object_or_404
# import requests
# from users.forms import signupForm
#
#
# # Create your views here.
#
# # def home3(request):
# #     return render(request, 'home/mainpage_logined.html')
# # def login(request):
# #     return render(request, 'login/login_page.html')
# #
# # def signup_page(request):
# #     return render(request, 'login/sign_up.html')
#
#
#
# # 회원가입
# def signup(request):
#     if request.method == "GET":
#         userForm = signupForm()
#         print("get 방식 이동")
#         return render(request, 'login/sign_up.html', {'userForm': userForm})
#     elif request.method == "POST":
#         userForm = signupForm(request.POST)
#         print("pass")
#         if userForm.is_valid():
#             print("data 통과")
#             if request.POST["password1"] == request.POST["password2"]:
#                 userForm.save()
#                 print("DB저장")
#             # 민수야 위에서 password1이랑 password2가 같은지 확인했으니까, 만약 다를경우도 생각해줘야할듯.
#             else:
#               print("비밀번호 불일치")
#               return render(request, 'login/fail.html')
#             return render(request, 'login/success.html')
#         else:
#             print("양식 오류")
#             return render(request, 'login/fail.html')
#
#
# def userlogin(request):
#     if request.method == "GET":
#         print('get 방식 이동')
#         loginForm = AuthenticationForm()
#         return render(request, 'login/login_page.html',
#                       {'loginForm': loginForm})
#     elif request.method == "POST":
#         print('POST 성공')
#         loginForm = AuthenticationForm(request, request.POST)
#         if loginForm.is_valid():
#             print('로그인 성공')
#             auth_login(request, loginForm.get_user())
#             return redirect('/')
#         else:
#             print('로그인 실패')
#             return render(request,'login/error.html')
#
# def userlogout(request):
#     auth_logout(request)
#     return redirect('/')

