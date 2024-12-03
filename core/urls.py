from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('estudantes/', EstudantesView.as_view(), name='estudantes'),
    path('ocupacoes/', OcupacoesView.as_view(), name='ocupacoes'),
    path('instituicoes/', InstituicoesView.as_view(), name='instituicoes'),
    path('areassaber/', AreasSaberView.as_view(), name='areassaber'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('turnos/', TurnosView.as_view(), name='turnos'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencias'),
    path('turmas/', TurmasView.as_view(), name='turmas'),
    path('ufs/', UFsView.as_view(), name='ufs'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencias'),
]