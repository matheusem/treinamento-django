# Generated by Django 3.0.5 on 2021-01-05 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaborador', '0007_auto_20210105_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='nome',
            field=models.CharField(default='DEFAULT VALUE', max_length=500),
        ),
    ]
