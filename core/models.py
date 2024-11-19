from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    nome_do_pai = models.CharField(max_length=100, verbose_name='Nome do pai')
    nome_da_mae = models.CharField(max_length=100, verbose_name='Nome da mãe')
    cpf = models.CharField(max_length=12, verbose_name='CPF')
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    email = models.CharField(max_length=200, verbose_name='E-mail')
    # cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE, verbose_name='Cidade da pessoa')
    ocupacao = models.ForeignKey("OcupacaoPessoas", on_delete=models.CASCADE, verbose_name='Ocupação da pessoa')


class OcupacaoPessoas(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Ocupação de pessoas')


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Instituição')
    site = models.CharField(max_length=200, verbose_name='Site')
    telefone = models.CharField(max_length=21, verbose_name='Telefone')#+55 (35) 99250-2080
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE, verbose_name='Cidade')


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Area')


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Curso')
    carga_horaria_total = models.IntegerField(verbose_name='Carga Horaria Total')
    duracao_meses = models.IntegerField(verbose_name='Duração em Meses')
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name='Área do Saber')
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name='Instituição de Ensino')


class Turno(models.Model):
    TURNO_CHOICES = (
        ('Matutino', 'Matutino'),
        ('Verspertino', 'Verspertino'),
        ('Noturno', 'Noturno'),
        ('Integral', 'Integral'),
    )
    nome = models.CharField(max_length=11, choices=TURNO_CHOICES, verbose_name='Turno')


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name='Área do Saber')


class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name='Instituição de Ensino')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    data_inicio = models.DateField()


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    nota = models.IntegerField(verbose_name='Nota')
    tipoavaliacao = models.ForeignKey("TipoAvaliacao", on_delete=models.CASCADE, verbose_name='Tipo da Avaliação')


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')
    numero_faltas = models.IntegerField(verbose_name='Numero de Faltas')


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Cidade')
    uf = models.CharField(max_length=2, verbose_name='Unidade Federativa')

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    data = models.DateField(verbose_name='Data de aplicação')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')

class DisciplinaPorCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')
    carga_horaria = models.IntegerField(verbose_name='Carga Horária')


class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Tipo da Avaliação')