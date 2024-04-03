from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenido a 3er año")

def about(request):
    return HttpResponse("About")