# Generated by Django 2.0.1 on 2018-02-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0005_registro_examen'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_examen',
            name='aldea',
            field=models.CharField(default='Aldea Kono', max_length=30),
        ),
        migrations.AlterField(
            model_name='registro_examen',
            name='date',
            field=models.DateField(),
        ),
    ]
