# Generated by Django 4.2.6 on 2024-07-21 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievement', '0005_rename_main_achievement_id_mainachievement_main_achievement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achievement',
            name='is_main',
        ),
    ]
