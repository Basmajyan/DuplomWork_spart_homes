# Generated by Django 4.0 on 2022-03-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_action_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Communal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mounth', models.CharField(blank=True, max_length=25, verbose_name='Месяц')),
                ('author', models.CharField(blank=True, max_length=100, verbose_name='ИД автора')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата и время')),
            ],
        ),
    ]