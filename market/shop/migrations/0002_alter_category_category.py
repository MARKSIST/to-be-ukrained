# Generated by Django 4.0.6 on 2022-08-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
