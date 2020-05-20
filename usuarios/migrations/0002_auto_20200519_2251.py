# Generated by Django 3.0.4 on 2020-05-19 22:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='perfil', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'gif'], code='imagen_invalida', message='Solo se permiten imagenes png, gif')], verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rfc',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(code='rfc_invalido', message='El RFC no tiene un formato valido', regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])) ?(?:- ?)?([A-Z\\d]{2})([A\\d])$')], verbose_name='R.F.C.'),
        ),
    ]