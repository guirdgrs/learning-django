from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Uma view function é uma função que recebe um pedido e retorna uma resposta ao cliente
# É um manipulador de solicitações

# Essa função deve ter um request e retornar um response
def say_hello(request):
    # Aqui é possível trazer dados do DB / Transformar esses dados / Mandar e-mail
    return HttpResponse('Hello World!')