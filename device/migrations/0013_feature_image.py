# Generated by Django 2.0.4 on 2018-06-22 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neptune', '0001_initial'),
        ('device', '0012_remove_feature_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neptune.SharedImage'),
        ),
    ]
