# Generated by Django 3.1.4 on 2021-04-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='desc',
            field=models.TextField(max_length=101, null=True),
        ),
    ]