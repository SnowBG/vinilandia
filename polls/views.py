from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Colé zé! Aqui é um índice de polls.")
