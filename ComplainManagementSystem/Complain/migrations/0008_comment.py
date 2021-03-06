# Generated by Django 3.0.3 on 2020-09-22 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_auto_20200922_0106'),
        ('Complain', '0007_auto_20200922_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Complain.Complain')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student')),
            ],
        ),
    ]
