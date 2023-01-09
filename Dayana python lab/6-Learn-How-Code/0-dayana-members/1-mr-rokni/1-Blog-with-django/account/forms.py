from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError


# Create your class form for login

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))

# Check authentication password
    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')

# Create UserEdit form
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')










# class RegisterForm(forms.Form):
#     username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input100'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100'}))
#
#     def clean_username(self):
#         user = authenticate(usernamee=self.cleaned_data.get('username'), password1=self.cleaned_data.get('password1'))
#         if user is None:
#             return self.cleaned_data.get('password1')
#         raise ValidationError('user has existed', code='user_existed')
#
#
#     # def clean_password1(self):
#     #     if password1 == password2:
    #         raise ValidationError('passwords are same')
