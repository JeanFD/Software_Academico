from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    nome_do_pai = models.CharField(max_length=100, verbose_name='Nome do pai')
    nome_da_mae = models.CharField(max_length=100, verbose_name='Nome da mãe')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    data_nasc = models.DateField(verbose_name='Data de Nascimento')
    email = models.CharField(max_length=200, verbose_name='E-mail')
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE, verbose_name='Cidade da pessoa', null=True)
    ocupacao = models.ForeignKey("OcupacaoPessoas", on_delete=models.CASCADE, verbose_name='Ocupação da pessoa')

    class meta:
        abstract = True

    def __str__(self):
        return self.nome


class Estudante(Pessoa):
    ra = models.CharField(max_length=16, verbose_name='Registro Acadêmico')
    turma = models.ForeignKey("Turma", on_delete=models.CASCADE, verbose_name='Turma')

    class meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class OcupacaoPessoas(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Ocupação de pessoas')

    class meta:
        verbose_name = 'Ocupação da Pessoa'
        verbose_name_plural = 'Ocupações das Pessoas'
    
    def __str__(self):
        return self.nome

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Instituição')
    site = models.CharField(max_length=200, verbose_name='Site')
    telefone = models.CharField(max_length=21, verbose_name='Telefone')#+55 (35) 99250-2080
    cidade = models.ForeignKey("Cidade", on_delete=models.CASCADE, verbose_name='Cidade')

    def __str__(self):
        return self.nome

class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Area')
    class meta:
            verbose_name = 'Area do Saber'
            verbose_name_plural = 'Areas do Saber'

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Curso')
    carga_horaria_total = models.IntegerField(verbose_name='Carga Horaria Total')
    duracao_meses = models.IntegerField(verbose_name='Duração em Meses')
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name='Área do Saber')
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name='Instituição de Ensino')

    def __str__(self):
        return self.nome
    

class Turno(models.Model):
    nome = models.CharField(max_length=11, verbose_name='Turno')

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name='Área do Saber')

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name='Instituição de Ensino')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, verbose_name='Pessoa', null=True)
    data_inicio = models.DateField()

    def __str__(self):
        return f'{self.estudante}, {self.curso}, {self.instituicao}'

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    nota = models.IntegerField(verbose_name='Nota')
    tipoavaliacao = models.ForeignKey("TipoAvaliacao", on_delete=models.CASCADE, verbose_name='Tipo da Avaliação')

    def __str__(self):
        return f'Avaliação de {self.disciplina} do curso de {self.curso}'


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE, verbose_name='Pessoa', null=True)
    numero_faltas = models.IntegerField(verbose_name='Numero de Faltas')

    def __str__(self):
        return f'{self.estudante}, {self.numero_faltas}'

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')

    def __str__(self):
        return self.nome

class UF(models.Model):
    sigla = models.CharField(max_length=2, verbose_name='Unidade Federativa')

    def __str__(self):
        return self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Cidade')
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, verbose_name='Unidade Federativa')

    def __str__(self):
        return self.nome

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    data = models.DateField(verbose_name='Data de aplicação')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name='Pessoa')

    def __str__(self):
        return self.descricao

class DisciplinaPorCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name='Disciplina')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name='Turno')
    carga_horaria = models.IntegerField(verbose_name='Carga Horária')

    def __str__(self):
        return f'{self.disciplina} {self.curso}'

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Tipo da Avaliação')

    def __str__(self):
        return self.nome