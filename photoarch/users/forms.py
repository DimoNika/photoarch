from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class LoginUserForm(forms.Form):

    username = forms.CharField(label="Username",
        widget=forms.widgets.TextInput(attrs={"class": "form-control", 
                                              "type":"username", 
                                              "id":"username", 
                                              "placeholder":"Username"}))
    

    password = forms.CharField(label="Password",
        widget=forms.widgets.PasswordInput(attrs={"class": "form-control",    
                                                  "type":"password", 
                                                  "id":"password", 
                                                  "placeholder":"Password"}))
    
class MyRegistreForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super(MyRegistreForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username', 'type': 'password'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})
    pass