# Generated by Django 4.0 on 2022-03-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_solution_authorid'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='solution',
            field=models.CharField(default=1, max_length=100, verbose_name='Решение для УД'),
            preserve_default=False,
        ),
    ]
