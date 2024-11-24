# Generated by Django 5.1.3 on 2024-11-24 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_turmas_turma_ocorrencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2, verbose_name='Unidade Federativa')),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.cidade', verbose_name='Cidade da pessoa'),
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.pessoa')),
                ('RA', models.CharField(max_length=16, verbose_name='Registro Acadêmico')),
                ('Turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.turma', verbose_name='Turma')),
            ],
            bases=('core.pessoa',),
        ),
        migrations.AlterField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.uf', verbose_name='Unidade Federativa'),
        ),
    ]