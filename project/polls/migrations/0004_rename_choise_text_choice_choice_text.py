# Generated by Django 4.1 on 2023-03-19 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_answer_choice_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choise_text',
            new_name='choice_text',
        ),
    ]