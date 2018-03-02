from django import forms
from django.contrib.auth.models import User
from registration_page.models import UsersProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model= User
        fields= ('first_name','last_name','username','password','confirm_password','email')

    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('password and confirm password does not match')