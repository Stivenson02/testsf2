from django.http import HttpResponse

def saludo(request):

    return HttpResponse("Hello WORLD")

def despedida(request, number):

    return HttpResponse("el numero es %s"%(number))