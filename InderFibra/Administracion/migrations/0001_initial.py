# Generated by Django 3.2.16 on 2022-12-22 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Valor', models.IntegerField()),
                ('Stock', models.IntegerField()),
                ('photo', models.ImageField(help_text=None, upload_to='static')),
                ('Ventas', models.IntegerField(default=0)),
                ('Marca', models.CharField(max_length=25)),
                ('Descripcion', models.TextField(max_length=250)),
                ('Modelo', models.CharField(max_length=50)),
            ],
        ),
    ]