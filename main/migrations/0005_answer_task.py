# Generated by Django 3.1.2 on 2020-12-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201214_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.task'),
        ),
    ]
