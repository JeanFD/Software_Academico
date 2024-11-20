from django.contrib import admin
from .models import *

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1



class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [OcupacaoInline]

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [PessoaInline]

admin.site.register(Pessoa)
admin.site.register(OcupacaoPessoas, OcupacaoAdmin)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(Turno)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Frequencia)
admin.site.register(Turma)
admin.site.register(Cidade)
admin.site.register(Ocorrencia)
admin.site.register(DisciplinaPorCurso)
admin.site.register(TipoAvaliacao)