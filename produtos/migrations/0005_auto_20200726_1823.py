# Generated by Django 3.0.8 on 2020-07-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_auto_20200726_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto_produto',
            field=models.ImageField(blank=True, upload_to='fotos/'),
        ),
    ]