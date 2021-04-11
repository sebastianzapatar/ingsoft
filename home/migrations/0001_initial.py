# Generated by Django 3.0.5 on 2021-04-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='nombre de la cancion', max_length=50)),
                ('autor', models.CharField(help_text='Quien escribio la cancion', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Canciones',
            },
        ),
    ]