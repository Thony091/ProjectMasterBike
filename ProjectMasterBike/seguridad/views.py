from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login(request):
    template_name = "login.html"
    response_data = {}
    if request.POST.get('action') =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(username=username, password=password)
        if user:
            print("usuario registrado")            
        else:
            print("Usuario no existe en la base de datos.")
    return render(request,template_name)