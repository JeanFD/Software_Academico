# Generated by Django 5.1.3 on 2024-11-26 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_uf_pessoa_cidade_aluno_alter_cidade_uf'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aluno',
            new_name='Estudante',
        ),
        migrations.RemoveField(
            model_name='frequencia',
            name='pessoa',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='pessoa',
        ),
        migrations.AddField(
            model_name='frequencia',
            name='estudante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.estudante', verbose_name='Pessoa'),
        ),
        migrations.AddField(
            model_name='matricula',
            name='estudante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.estudante', verbose_name='Pessoa'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='nome',
            field=models.CharField(max_length=11, verbose_name='Turno'),
        ),
    ]