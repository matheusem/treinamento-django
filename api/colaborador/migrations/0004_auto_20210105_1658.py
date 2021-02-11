# Generated by Django 3.0.5 on 2021-01-05 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0003_colaborador_data_nascimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=500)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.AddField(
            model_name='colaborador',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='curriculo',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='Colaboradores', verbose_name='Foto do Colaborador'),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº de telefone'),
        ),
    ]