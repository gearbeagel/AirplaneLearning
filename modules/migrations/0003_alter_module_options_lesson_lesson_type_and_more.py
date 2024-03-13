# Generated by Django 5.0.3 on 2024-03-13 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_lesson_rename_name_module_title_module_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('Q', 'Quiz'), ('I', 'Informational')], default='I', max_length=1),
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='modules.module'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='not_started', max_length=20),
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='module',
            name='lessons',
            field=models.ManyToManyField(related_name='modules', to='modules.lesson'),
        ),
    ]