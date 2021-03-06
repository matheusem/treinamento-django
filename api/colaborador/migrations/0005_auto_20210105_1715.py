# Generated by Django 3.0.5 on 2021-01-05 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0004_auto_20210105_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='Cargo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colaborador.Cargo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='colaborador',
            name='Genero',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colaborador.Genero'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nome',
            field=models.CharField(default="DEFAULT VALUE", max_length=500),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='salario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='genero',
            name='nome',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
