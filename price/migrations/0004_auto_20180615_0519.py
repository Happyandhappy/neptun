# Generated by Django 2.0.4 on 2018-06-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_auto_20180614_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='marketshare',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='spend',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='discount',
            name='units',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Discount by percent'), (2, 'Discount by Dollar Value')], default=1, verbose_name='Discount type'),
        ),
    ]
