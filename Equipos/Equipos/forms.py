from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                             max_length=50, min_length=4,
                             widget=forms.TextInput(attrs={
                                 'class':'form-control',
                                 'id':'nombre',
                                 'placeholder':'Nombre/registro'
                             }))
    email =forms.EmailField(required=True,
                            max_length=50, min_length=4,
                             widget=forms.EmailInput(attrs={
                                 'class':'form-control',
                                 'id':'email',
                                 'placeholder':'asddsada@gmail.com'
                         }))
    password =forms.CharField(required=True,
                            max_length=50, min_length=4,
                            widget=forms.PasswordInput(attrs={
                                 'class':'form-control',
                                 'id':'contraseña',
                                 'placeholder':'contraseña'
                             }))
    password2 =forms.CharField(label='Confirmar password',
                            required=True,
                            max_length=50, min_length=4,
                            widget=forms.PasswordInput(attrs={
                                 'class':'form-control',
                                 'id':'contraseña2',
                                 'placeholder':'Confirmar contraseña'
                             }))
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email
    
    def clean(self):
        cleaned_data=super().clean()
        
        if cleaned_data.get('password2')!= cleaned_data.get('password'):
            self.add_error('password2','El password no coincide')
            
    def save(self):
        User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
        )