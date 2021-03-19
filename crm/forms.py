from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=12, label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
