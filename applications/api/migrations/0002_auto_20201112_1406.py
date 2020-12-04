# Generated by Django 3.1.3 on 2020-11-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='reason',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('0', 'Creada'), ('1', 'Asignada'), ('2', 'Cancelada'), ('3', 'En proceso'), ('4', 'Pendiente'), ('5', 'En revisión'), ('6', 'Finalizada')], max_length=1, verbose_name='Estado'),
        ),
    ]