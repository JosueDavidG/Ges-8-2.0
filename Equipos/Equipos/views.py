from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
from inventario.models import productos,Ropa,productosImplementos,tamaños,ImplementosDeportivos



def index(request):
    return render(request, 'inicio.html',{
      'mensaje':'Nuevo mensaje desde View.py',
      'tittle':'titulo',
      'equipos':[
          {'nombre':'bayer','escudo':'Ilegible','bandera':True},
          {'nombre':'bayer','escudo':'Ilegible','bandera':True},
          {'nombre':'bayer','escudo':'Ilegible','bandera':False},
      ]
    })


def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'Bienvenido'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'No se pudo logear de manera correcta')
    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'Sesion cerrada exitosamente')
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
      username =  form.cleaned_data.get('username')
      email = form.cleaned_data.get('email')
      password =  form.cleaned_data.get('password')
      
      user = User.objects.create_user(username,email,password)
      if user:
          login(request, user)
          messages.success(request,'Usuario creado exitosamente')
          return redirect('index')
    return render(request, 'users/register.html',{
        'form':form
    })

def inventario_view(request):
    productoss = productos.objects.all().order_by()
    
    return render(request, 'jugadores.html',{
      'mensaje':'Nuevo mensaje desde View.py',
      'nombre':'nombre',
      'jugadores':productoss,
    })

def inventario_view(request):
    productoss = productos.objects.all().order_by()
    
    return render(request, 'jugadores.html',{
      'mensaje':'Nuevo mensaje desde View.py',
      'nombre':'nombre',
      'jugadores':productoss,
    })
def inventario_view(request):
    productoss = productos.objects.all().order_by()
    
    return render(request, 'jugadores.html',{
      'mensaje':'Nuevo mensaje desde View.py',
      'nombre':'nombre',
      'jugadores':productoss,
    })
def inventario_view(request):
    productoss = productos.objects.all().order_by()
    
    return render(request, 'jugadores.html',{
      'mensaje':'Nuevo mensaje desde View.py',
      'nombre':'nombre',
      'jugadores':productoss,
    })
def inventario_view(request):
    productoss = productos.objects.all().order_by()
    
    return render(request, 'jugadores.html',{
      'mensaje':'Nuevo mensaje desde View.py',
      'nombre':'nombre',
      'jugadores':productoss,
    })
def inventario_view(request):
    productoss = productos.objects.all().order_by()
    
    return render(request, 'jugadores.html',{
      'mensaje':'Nuevo mensaje desde View.py',
      'nombre':'nombre',
      'jugadores':productoss,
    })