# Generated by Django 4.0 on 2022-03-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_solution_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectedSolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100, verbose_name='ИД автора')),
                ('solutionID', models.CharField(max_length=100, verbose_name='ИД решение УД')),
                ('status', models.CharField(choices=[('none', 'none'), ('treatment', 'В обработке'), ('connected', 'Подключено')], default='none', max_length=60, null=True, verbose_name='Статус')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
        migrations.RemoveField(
            model_name='solution',
            name='author',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='status',
        ),
    ]
