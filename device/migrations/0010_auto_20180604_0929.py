# Generated by Django 2.0.4 on 2018-06-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0009_auto_20180529_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryfeature',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='features/', verbose_name='Feature image'),
        ),
        migrations.AddField(
            model_name='feature',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='features/', verbose_name='Feature image'),
        ),
    ]
