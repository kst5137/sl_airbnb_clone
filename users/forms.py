from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["u_phonenum", 'u_address','u_sex']



    def signup(self, request, user):
        user.u_phonenum = self.cleaned_data['u_phonenum']
        user.u_address = self.cleaned_data['u_address']
        user.u_sex = self.cleaned_data['u_sex']
        user.save()

