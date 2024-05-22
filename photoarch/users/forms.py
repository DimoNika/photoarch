from django import forms


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