# Generated by Django 2.0.1 on 2018-02-26 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0003_auto_20180226_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_mision', models.CharField(max_length=20)),
                ('lugar', models.CharField(max_length=20)),
                ('rango', models.CharField(max_length=1)),
                ('status_mision', models.BooleanField()),
                ('equipo_encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.EquipoNinja')),
            ],
        ),
    ]
