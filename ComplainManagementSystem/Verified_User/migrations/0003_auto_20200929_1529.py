# Generated by Django 3.0.3 on 2020-09-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verified_User', '0002_verified_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verified_user',
            name='status',
            field=models.CharField(choices=[('Verified', 'Verified'), ('Not Verified', 'Not Verified')], default='Not Verified', max_length=100),
        ),
    ]
