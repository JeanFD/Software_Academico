from django.contrib import admin
from .models import *

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

# class DisciplinaInline(admin.TabularInline):
#     model = Disciplina
#     extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class EstudantesInline(admin.TabularInline):
    model = Estudante
    extra = 1

class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = DisciplinaPorCurso
    extra = 1



class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [PessoaInline]

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [CursoInline]

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [CursoInline]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [AvaliacaoInline]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [EstudantesInline]

class UfAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [CidadeInline]

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    inlines = [CursoDisciplinaInline]


admin.site.register(Estudante)
admin.site.register(OcupacaoPessoas, OcupacaoAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turno)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Matricula)
admin.site.register(Frequencia)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Cidade)
admin.site.register(UF)
admin.site.register(Ocorrencia)
admin.site.register(DisciplinaPorCurso)
admin.site.register(TipoAvaliacao)