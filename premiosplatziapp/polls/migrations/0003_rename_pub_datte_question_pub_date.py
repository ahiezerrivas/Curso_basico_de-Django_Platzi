# Generated by Django 4.0.5 on 2022-06-09 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choices_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_datte',
            new_name='pub_date',
        ),
    ]
