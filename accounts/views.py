from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def vw_acc_new(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    
    else:
        user_form = UserCreationForm()

    return render(request, 'accounts/new.html', {'user_form': user_form})

