# Generated by Django 4.1.3 on 2022-11-21 20:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_contato_foto_alter_contato_datacriacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='datacriacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
