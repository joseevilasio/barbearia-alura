# Generated by Django 3.0.8 on 2020-08-04 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_contatos'),
    ]

    operations = [
        migrations.AddField(
            model_name='contatos',
            name='data_envio',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 22, 16, 58, 817466)),
        ),
    ]
