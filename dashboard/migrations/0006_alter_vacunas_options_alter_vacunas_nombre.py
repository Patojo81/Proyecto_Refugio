# Generated by Django 4.0.3 on 2022-05-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_mascotas_vacuna'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacunas',
            options={'verbose_name_plural': 'Vacunas'},
        ),
        migrations.AlterField(
            model_name='vacunas',
            name='Nombre',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
