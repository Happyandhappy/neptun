# Generated by Django 2.0.4 on 2018-07-05 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0032_item_cost_type'),
        ('device', '0019_auto_20180625_0916'),
        ('tracker', '0003_auto_20180705_0731'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchaseprice',
            unique_together={('category', 'client', 'year', 'level', 'cost_type')},
        ),
    ]
