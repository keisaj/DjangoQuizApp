# Generated by Django 4.0.3 on 2022-03-18 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0005_alter_question_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
