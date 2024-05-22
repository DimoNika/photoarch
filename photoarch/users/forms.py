from django import forms


class LoginUserForm(forms.Form):
    username = forms.EmailField(label="Email",
                                widget=forms.widgets.TextInput(attrs={"class": "form-input"}))
    password = forms.EmailField(label="Password",
                                widget=forms.widgets.PasswordInput(attrs={"class": "form-input"}))