# Generated by Django 4.1 on 2022-09-09 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diaristas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('telefone', models.CharField(max_length=11)),
                ('logradouro', models.CharField(max_length=60)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=30)),
                ('complemento', models.CharField(blank=True, max_length=100)),
                ('cep', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
                ('codigo_ibge', models.IntegerField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
    ]
