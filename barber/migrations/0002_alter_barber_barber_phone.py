# Generated by Django 4.1.2 on 2022-10-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='barber_phone',
            field=models.IntegerField(),
        ),
    ]
