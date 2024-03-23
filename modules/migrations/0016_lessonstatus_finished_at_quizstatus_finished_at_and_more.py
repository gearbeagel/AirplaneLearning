# Generated by Django 5.0.3 on 2024-03-23 12:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0015_alter_quizstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonstatus',
            name='finished_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizstatus',
            name='finished_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lessonstatus',
            name='status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='not_started', max_length=20),
        ),
    ]
