from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class VRegistro(View):

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})              

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Inicio')  
        return render(request, "registro/registro.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Inicio')

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Inicio')
            else:
                return render(request, "login/login.html", {"form": form})
        else:
            return render(request, "login/login.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "login/login.html", {"form": form})