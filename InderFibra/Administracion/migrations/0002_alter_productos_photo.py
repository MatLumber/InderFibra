# Generated by Django 3.2.16 on 2022-12-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='photo',
            field=models.ImageField(help_text=None, upload_to='Principal/static'),
        ),
    ]