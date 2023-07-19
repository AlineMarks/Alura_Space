from django.shortcuts import render
from usuario.forms import LoginForms,CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth


def login (request):
    form = LoginForms()
    dados = {
        'form':form
    }
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['nome_login'].value()
            senha=form['senha'].value()
            usuario = auth.authenticate(request, username = nome, passoword = senha
            )
            if User.objects.filter(username=nome).exists():        
                if usuario is not None:
                    auth.login(request, usuario)
                    print('deu certo login')
                    return render (request, 'galeria/index.html')         
                else:
                    print('não deu certo login')
                    return render(request,'usuarios/login.html')
            
    return render (request, 'usuarios/login.html', dados)



def cadastro (request):
   form = CadastroForms()
   dados = {
      'form':form
   }
   if request.method == 'POST':
       form = CadastroForms(request.POST)
       if form.is_valid(): 
            if form['senha_1'].value() != form['senha_2'].value():
                return render (request, 'usuarios/cadastro.html')
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            
            if User.objects.filter (username=nome).exists():
                return render (request, 'usuarios/cadastro.html')
            else:
                usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
                usuario.save()
                return render (request, 'galeria/index.html')       
              

   return render (request, 'usuarios/cadastro.html', dados)