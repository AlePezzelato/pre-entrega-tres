# Generated by Django 5.0.6 on 2024-05-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]