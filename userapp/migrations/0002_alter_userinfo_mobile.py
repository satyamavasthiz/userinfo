# Generated by Django 4.1 on 2024-08-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Mobile',
            field=models.BigIntegerField(),
        ),
    ]
