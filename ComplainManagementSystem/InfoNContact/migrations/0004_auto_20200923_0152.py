# Generated by Django 3.1.1 on 2020-09-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfoNContact', '0003_auto_20200923_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone_no',
            field=models.IntegerField(unique=True),
        ),
    ]
