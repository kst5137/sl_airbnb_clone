from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # 사용할 모델
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

class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        exclude = ()

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        exclude = ()

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        exclude = ()

class SafetyForm(forms.ModelForm):
    class Meta:
        model = Safety
        exclude = ()

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        exclude = ('product', 'user',)