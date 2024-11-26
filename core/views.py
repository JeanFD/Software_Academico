from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
class EstudantesView(View):
    def get(self,request):
        contexto = {
            'estudantes': Estudante.objects.all(),
        }
        return render(request, 'estudantes.html', contexto)
# Create your views here.
