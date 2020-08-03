# Generated by Django 3.0.8 on 2020-07-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('descricao_produto', models.CharField(max_length=400)),
                ('preco_produto', models.DecimalField(decimal_places=10, max_digits=19)),
                ('foto_produto', models.ImageField(blank=True, upload_to='fotos/')),
            ],
        ),
    ]
