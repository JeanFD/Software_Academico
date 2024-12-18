# Generated by Django 5.1.3 on 2024-11-19 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaSaber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Area')),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='Unidade Federativa')),
            ],
        ),
        migrations.CreateModel(
            name='OcupacaoPessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Ocupação de pessoas')),
            ],
        ),
        migrations.CreateModel(
            name='TipoAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Tipo da Avaliação')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('Matutino', 'Matutino'), ('Verspertino', 'Verspertino'), ('Noturno', 'Noturno'), ('Integral', 'Integral')], max_length=11, verbose_name='Turno')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da disciplina')),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.areasaber', verbose_name='Área do Saber')),
            ],
        ),
        migrations.CreateModel(
            name='InstituicaoEnsino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome da Instituição')),
                ('site', models.CharField(max_length=200, verbose_name='Site')),
                ('telefone', models.CharField(max_length=21, verbose_name='Telefone')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cidade', verbose_name='Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Curso')),
                ('carga_horaria_total', models.IntegerField(verbose_name='Carga Horaria Total')),
                ('duracao_meses', models.IntegerField(verbose_name='Duração em Meses')),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.areasaber', verbose_name='Área do Saber')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instituicaoensino', verbose_name='Instituição de Ensino')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('nome_do_pai', models.CharField(max_length=100, verbose_name='Nome do pai')),
                ('nome_da_mae', models.CharField(max_length=100, verbose_name='Nome da mãe')),
                ('cpf', models.CharField(max_length=12, verbose_name='CPF')),
                ('data_nasc', models.DateField(verbose_name='Data de Nascimento')),
                ('email', models.CharField(max_length=200, verbose_name='E-mail')),
                ('ocupacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ocupacaopessoas', verbose_name='Ocupação da pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso', verbose_name='Curso')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.instituicaoensino', verbose_name='Instituição de Ensino')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa', verbose_name='Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_faltas', models.IntegerField(verbose_name='Numero de Faltas')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina', verbose_name='Disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa', verbose_name='Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('nota', models.IntegerField(verbose_name='Nota')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina', verbose_name='Disciplina')),
                ('tipoavaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoavaliacao', verbose_name='Tipo da Avaliação')),
            ],
        ),
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turno', verbose_name='Turno')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaPorCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.IntegerField(verbose_name='Carga Horária')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina', verbose_name='Disciplina')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turno', verbose_name='Turno')),
            ],
        ),
    ]
