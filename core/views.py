from django.shortcuts import render

def HomeView(request):
    return render(request, 'home.html')

def ProfileView(request, username):
    return render(request, 'profile.html', {
        'user': username
    })
