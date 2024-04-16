# Generated by Django 5.0.4 on 2024-04-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Article', 'Article'), ('Video', 'Video'), ('Other', 'Other')], default='Other', max_length=100)),
                ('source', models.URLField(max_length=500)),
            ],
        ),
    ]
