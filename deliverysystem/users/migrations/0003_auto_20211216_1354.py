# Generated by Django 3.2.9 on 2021-12-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211216_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
