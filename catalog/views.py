from django.shortcuts import render

def home_html(request):
    return render(request, 'home.html')

def contacts_html(request):
    return render(request, 'contacts.html')