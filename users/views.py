from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        forms = UserRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('users:login')
    else:
        forms = UserRegistrationForm()       
        messages.error(request, 'Error creating account. Please try again.')
    return render(request, 'users/register.html', {'form': forms})


def logout_view(request):
    logout(request)
    return redirect('users:login')   
