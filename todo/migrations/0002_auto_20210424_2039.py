# Generated by Django 3.1.4 on 2021-04-24 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='desc',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
