# Generated by Django 3.1.2 on 2020-12-14 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_of_finish', models.DateField(auto_now=True, verbose_name='Дата завершения')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Урок')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Группа(учебная)',
                'verbose_name_plural': 'Группы(учебная)',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=50)),
                ('monday', models.CharField(max_length=50)),
                ('tuesday', models.CharField(max_length=50)),
                ('wednesday', models.CharField(max_length=50)),
                ('thursday', models.CharField(max_length=50)),
                ('friday', models.CharField(max_length=50)),
                ('saturday', models.CharField(max_length=50)),
                ('sunday', models.CharField(max_length=50)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.group')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Задание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_of_start', models.DateField(verbose_name='Дата начала')),
                ('date_of_finish', models.DateField(null=True, verbose_name='Дата завершения')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.discipline')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.group')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(verbose_name='Оценка')),
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.answer')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
    ]
