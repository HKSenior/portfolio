from django import forms

from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        )
    )
    phoneNumber = PhoneNumberField(
        widget=PhoneNumberInternationalFallbackWidget(
            attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Phone Number',
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            }
        )
    )
