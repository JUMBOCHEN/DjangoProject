from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserInfo

class LoginForm(forms.Form):    #登录表单类
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):    #用户注册表单类
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("password do not match.")
        return cd['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'birth')

class UserInfoForm(forms.ModelForm):
    class Mete:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)
