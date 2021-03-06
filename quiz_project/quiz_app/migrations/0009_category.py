# Generated by Django 4.0.3 on 2022-03-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0008_alter_question_correct_answer_alter_question_option1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[(0, 'Other'), (1, 'Music'), (2, 'Science'), (3, 'Literature'), (4, 'Movies'), (5, 'Sports')], default=0, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
