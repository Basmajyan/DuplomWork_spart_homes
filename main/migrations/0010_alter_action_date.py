# Generated by Django 4.0 on 2022-03-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время'),
        ),
    ]