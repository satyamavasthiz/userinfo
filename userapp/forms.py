from django import forms
from .models import userinfo

class userinfoform(forms.Form):
    UID=forms.IntegerField(
        label='UID',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'UID',
                'class':'form-control'
            }
        )
    )

    UName = forms.CharField(
        label='Enter User Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'User Name',
                'class': 'form-control'
            }
        )
    )

    Password = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'User Password',
                'class': 'form-control'
            }
        )
    )

    UType = forms.CharField(
        label='Enter User Type',
        widget=forms.ChoiceField(
            choices=UType_CHOICES
            attrs={
                'placeholder': 'User Type',
                'class': 'form-control'
            }
        )
    )

    Status = forms.CharField(
        label='',
        widget=forms.RadioSelect(
            attrs={

                'class': 'form-control'
            }
        )
    )

    Mobile = forms.IntegerField(
        label='Enter User Mobile',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'User Mobile',
                'class': 'form-control'
            }
        )
    )

    Email = forms.EmailField(
        label='Enter User Email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'User Email',
                'class': 'form-control'
            }
        )
    )

    Cdatatime = forms.DateTimeField(
        label='Enter Cdatetime',
        widget=forms.DateTimeInput(
            attrs={
                'placeholder': 'Date & Time',
                'class': 'form-control'
            }
        )
    )