from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['u_nickname','email',"u_phonenum", 'u_address','u_sex']


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["u_nickname", "u_phonenum", 'u_address','u_sex']



    def signup(self, request, user):
        user.u_nickname = self.cleaned_data['u_nickname']
        user.u_phonenum = self.cleaned_data['u_phonenum']
        user.u_address = self.cleaned_data['u_address']
        user.u_sex = self.cleaned_data['u_sex']
        user.save()

