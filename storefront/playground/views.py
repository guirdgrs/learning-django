from django.shortcuts import render
from django.http import HttpResponse

# Uma view function é uma função que recebe um pedido e retorna uma resposta ao cliente
# É mais um manipulador de solicitações do que uma 'view' de fato

# Essa função deve ter um request e retornar um response
def say_hello(request):
    # Aqui é possível trazer dados do DB / Transformar esses dados / Mandar e-mail
    return render(request, 'hello.html', {'name': 'Kuro'})
    # retorna um HttpResponse com o template renderizado e passa um name para o template