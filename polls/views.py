from django.http import HttpResponse

#metodo index
def index(request):
    return HttpResponse("<h1> Olá Mundo!!! </h1>")
