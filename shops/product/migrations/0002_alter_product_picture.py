# Generated by Django 4.0.6 on 2022-07-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='product/uploads'),
        ),
    ]
