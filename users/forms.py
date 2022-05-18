from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username','email',"u_phonenum", 'u_address','u_sex']
#
# class UpdateUserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','email',"u_phonenum", 'u_address','u_sex']
#
# class UpdateProfileForm(forms.ModelForm):
#     u_nickname = forms.CharField()
#     email = forms.CharField()
#     u_sex = forms.CharField()
#     birth_year = forms.CharField()
#     class Meta:
#         model = User
#         fields = ['username','email',"u_phonenum", 'u_address','u_sex']






class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["u_phonenum", 'u_address','u_sex']



    def signup(self, request, user):
        user.u_phonenum = self.cleaned_data['u_phonenum']
        user.u_address = self.cleaned_data['u_address']
        user.u_sex = self.cleaned_data['u_sex']
        user.save()

