from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UpdateProfileForm
from django.contrib import messages

# Create your views here.

def perfil(request, pk):
    perfil_usuario = UserProfile.objects.get(id_perfil=pk)
    context = {'perfil': perfil_usuario}
    return render(request, 'profiles/profile.html', context)

def conta(request):
    conta_usuario = request.user.userprofile
    context = {'conta': conta_usuario}
    return render(request, 'profiles/account.html', context)

def atualizarperfil(request):
    perfil = request.user.userprofile
    form = UpdateProfileForm(instance=perfil)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            messages.info(request, 'Você atualizou seu perfil!')
            return redirect('conta')
    context = {"form": form }
    return render(request, 'profiles/updateprofile.html', context)

def deletarperfil(request):
    perfil = request.user.userprofile
    form = UpdateProfileForm(instance=perfil)
    if request.method == 'POST':
        user = request.user
        user.delete()
    
        return redirect('index')
    context = {"form": form}
    return render(request, 'profiles/deleteprofile.html', context)