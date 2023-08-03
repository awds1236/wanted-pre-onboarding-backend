from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'join/join.html', {'form': form})
