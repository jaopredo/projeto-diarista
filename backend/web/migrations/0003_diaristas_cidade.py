# Generated by Django 4.1.2 on 2022-10-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_diaristas_cep'),
    ]

    operations = [
        migrations.AddField(
            model_name='diaristas',
            name='cidade',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
