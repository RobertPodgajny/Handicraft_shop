# Generated by Django 2.0.3 on 2018-03-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_auto_20180322_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.SmallIntegerField(choices=[(0, 'Metryczki'), (1, 'Ślubne')]),
        ),
    ]
