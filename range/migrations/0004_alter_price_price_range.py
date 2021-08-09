# Generated by Django 3.2.5 on 2021-08-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('range', '0003_alter_price_price_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price_range',
            field=models.IntegerField(choices=[(28, '0-1500'), (30, '1501-1750'), (33, '1751-2000')], max_length=10),
        ),
    ]
