# Generated by Django 2.0.1 on 2018-02-26 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_mision'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_misiones', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status_registro', models.BooleanField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipos.EquipoNinja')),
            ],
        ),
    ]
