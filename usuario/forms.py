from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length=100,
        widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'placeholder': 'Ex.: Juan Marques',
        }
        )
        )
    senha = forms.CharField(
        label = 'Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder': 'Digite sua senha',
        }
        )
        )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length=100,
        widget=forms.TextInput(
        attrs={'class':'form-control',
        'placeholder': 'Ex.: Juan Marques',
        })
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget = forms.EmailInput (
        attrs={
        'class':'form-control',
        'placeholder': 'juanmarques@gmail.com',
        })
    )
    senha_1 = forms.CharField(
        label = 'Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder': 'Digite sua senha',
        }
        )
    )
    senha_2 = forms.CharField(
        label = 'Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder': 'Digite sua senha novamente',
        }
        )
    )     