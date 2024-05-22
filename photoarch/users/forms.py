from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Username",
                                widget=forms.widgets.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Password",
                                widget=forms.widgets.PasswordInput(attrs={"class": "form-input"}))