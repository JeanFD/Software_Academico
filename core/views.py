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
    
class OcupacoesView(View):
    def get(self,request):
        contexto = {
            'ocupacoes': OcupacaoPessoas.objects.all(),
        }
        return render(request, 'ocupacoes.html', contexto)

class InstituicoesView(View):
    def get(self, request):
        contexto = {
            'instituicoes': InstituicaoEnsino.objects.all(),
        }
        return render(request, 'instituicoes.html', contexto)

class AreasSaberView(View):
    def get(self, request):
        contexto = {
            'areas': AreaSaber.objects.all(),
        }
        return render(request, 'areassaber.html', contexto)

class CursosView(View):
    def get(self, request):
        contexto = {
            'cursos': Curso.objects.all(),
        }
        return render(request, 'cursos.html', contexto)
    
class TurnosView(View):
    def get(self, request):
        contexto = {
            'turnos': Turno.objects.all(),
        }
        return render(request, 'turnos.html', contexto)

class DisciplinasView(View):
    def get(self, request):
        contexto = {
            'disciplinas': Disciplina.objects.all(),
        }
        return render(request, 'disciplinas.html', contexto)

class MatriculasView(View):
    def get(self, request):
        contexto = {
            'matriculas': Matricula.objects.all(),
        }
        return render(request, 'matriculas.html', contexto)
    
class AvaliacoesView(View):
    def get(self, request):
        contexto = {
            'avaliacoes': Avaliacao.objects.all(),
        }
        return render(request, 'avaliacoes.html', contexto)
    
class FrequenciasView(View):
    def get(self, request):
        contexto = {
            'frequencias': Frequencia.objects.all(),
        }
        return render(request, 'frequencias.html', contexto)
    
class TurmasView(View):
    def get(self, request):
        contexto = {
            'turmas': Turma.objects.all(),
        }
        return render(request, 'turmas.html', contexto)
    
class UFsView(View):
    def get(self, request):
        contexto = {
            'ufs': UF.objects.all(),
        }
        return render(request, 'ufs.html', contexto)
    
class CidadesView(View):
    def get(self, request):
        contexto = {
            'cidades': Cidade.objects.all(),
        }
        return render(request, 'cidades.html', contexto)

class OcorrenciasView(View):
    def get(self, request):
        contexto = {
            'ocorrencias': Ocorrencia.objects.all(),
        }
        return render(request, 'ocorrencias.html', contexto)


# Create your views here.
