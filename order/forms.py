from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # product = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city','username','product']

        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # self.fields['product'] = self.fields.get('product_id')
    #
    #
    #
    #     self.fields['product'].disabled = True





