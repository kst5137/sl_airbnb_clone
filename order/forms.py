from django import forms
from .models import Order



class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        # widgets = {'product' : forms.HiddenInput}

        
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
    #
        # self.fields['product'].initial = 'default value'
    #
        # self.fields['product'].disabled = True






