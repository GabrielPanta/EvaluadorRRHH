# Generated by Django 5.2.4 on 2025-07-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('experiencia', models.IntegerField()),
                ('habilidades', models.TextField()),
                ('estudios', models.CharField(max_length=100)),
                ('personalidad', models.CharField(max_length=100)),
            ],
        ),
    ]
