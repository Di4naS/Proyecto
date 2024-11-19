from django import forms
from .models import *
from django.contrib.auth.models import User

class contacto_form(forms.Form):
    correo =forms.EmailField(widget= forms.TextInput)
    titulo =forms.CharField(widget= forms.TextInput)
    texto =forms.CharField(widget= forms.Textarea)

class agregar_producto_form(forms.ModelForm):
    class Meta:
        model = Producto
        fields ='__all__'

 #class Meta:
  #      model = Producto
   #     fields = ['nombre', 'descripcion', 'status', 'precio', 'stock', 'categorias', 'marca', 'foto']
    #    widgets = {
     #       'precio': forms.TextInput(attrs={'readonly': 'readonly'}),
      #  }

class login_form(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'}))
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.TextInput())
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
    password_2 = forms.CharField(label='Confirmar Password', widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de Usuario ya registrado')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            email = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Correo Electronico ya existe') 
    
    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')  
        password_2 = self.cleaned_data.get('password_2')
        
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password_2