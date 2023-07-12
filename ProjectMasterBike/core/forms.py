from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Contacto, User, BikeUser

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreUsuario','apellidoUsuario','rutUsuario','emailUsuario','contraseniaUsuario','direccionUsuario', 'comuna']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombreCompleto', 'emailUsuario','asunto', 'mensaje']

class ClienteCreationForm(UserCreationForm):
    email = forms.EmailField(required=True) #exige rellenar para poder hacer validacion al terminar de registrar y compare con los correos existentes

    class Meta: #Meta define el comportamiento de la clase creada
        model = User #Toma de base campos de modelo "User" de django
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] #especifica los campos que se requeriran en el formulario proveniente de "UserCreationForm"
        # Método para comprobar si el email existe en la base de datos
        def clean_email(self):
            email = self.cleaned_data['email']

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este correo electrónico ya está registrado')
            return email

class RegistroBikeForm(ModelForm):
    class Meta:
        model = BikeUser
        fields = ['nombreDuenio', 'emailDuenio', 'fechaCompra', 'codBoleta', 'numChasis', 'rutDuenio','descripcion','comuna']
    