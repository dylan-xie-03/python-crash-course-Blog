# Generated by Django 3.1.4 on 2020-12-30 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20201230_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='text',
            field=models.TextField(max_length=400),
        ),
    ]
