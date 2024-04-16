# Generated by Django 5.0.4 on 2024-04-16 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0030_alter_profile_receive_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_modules_notifications', models.BooleanField(default=True)),
                ('quiz_results_notifications', models.BooleanField(default=True)),
                ('discussion_notifications', models.BooleanField(default=True)),
                ('new_resources_notifications', models.BooleanField(default=True)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profile_page.profile')),
            ],
        ),
    ]
