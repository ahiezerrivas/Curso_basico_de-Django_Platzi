# Generated by Django 4.0.5 on 2022-06-12 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_pub_datte_question_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question',
            new_name='question_text',
        ),
    ]
