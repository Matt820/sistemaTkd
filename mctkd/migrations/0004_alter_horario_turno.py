# Generated by Django 4.0.2 on 2024-01-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mctkd', '0003_alumno_apoderado_alumno_categoria_alumno_cinturon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='turno',
            field=models.CharField(max_length=10),
        ),
    ]
