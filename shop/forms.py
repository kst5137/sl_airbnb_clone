from django import forms
from .models import Product, Image

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # 사용할 모델
        exclude = ()

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ()

ImageFormSet = forms.inlineformset_factory(Product, Image, form=ImageForm, extra=5)
