from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['text text text text', '+7(983)123-43-21']})
