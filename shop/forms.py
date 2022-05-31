from django import forms
from .models import *
from django import forms
from django.urls import reverse_lazy
from .widgets import DatePickerWidget


from django import forms
from django.forms import ModelForm

from .models import Product


class DateInput(forms.DateInput):
    input_type = 'date'


class PromiseForm(ModelForm):

    class Meta:
        model = Product
        fields = ['writer', 'p_name', 'checkin', 'checkout']
        widgets = {
            'checkin': DatePickerWidget,
            'checkout': DatePickerWidget,
        }



class checkinForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            'checkin': DatePickerWidget,
            'checkout': DatePickerWidget,
        }
        exclude = ()

from bootstrap_datepicker_plus.widgets import DatePickerInput

from django import forms



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # 사용할 모델
        fields = '__all__'
        widgets = {
            'checkin': forms.DateInput(attrs={'type':'date'}),  # default date-format %m/%d/%Y will be used
            'checkout': forms.DateInput(attrs={'type':'date'}),  # specify date-frmat
        }
        exclude = ()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]

ImageFormSet = forms.inlineformset_factory(Product, Image, form=ImageForm, extra=5)

class RegisterProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ()

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        exclude = ()

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        exclude = ()

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        exclude = ('product', 'user',)