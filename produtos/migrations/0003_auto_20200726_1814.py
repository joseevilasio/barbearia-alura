# Generated by Django 3.0.8 on 2020-07-26 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20200726_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_produto',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
