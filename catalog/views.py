from django.shortcuts import render
from django.http import HttpResponse

def home_html(request):
    return render(request, 'home.html')

def contacts_html(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

    return render(request, 'contacts.html')