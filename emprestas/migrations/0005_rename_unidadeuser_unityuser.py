# Generated by Django 3.2.6 on 2021-10-27 14:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emprestas', '0004_auto_20211027_1142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UnidadeUser',
            new_name='UnityUser',
        ),
    ]
