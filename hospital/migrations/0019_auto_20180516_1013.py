# Generated by Django 2.0.4 on 2018-05-16 10:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0018_client_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'user account'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'user role'},
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('user', 'client')},
        ),
    ]
