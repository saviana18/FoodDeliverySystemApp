# Generated by Django 3.2.9 on 2021-12-16 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorRestaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('adress', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('menu_type', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.menu'),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('administrator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.administratorrestaurant')),
                ('restaurant_name', models.CharField(max_length=1000)),
                ('restaurant_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('restaurant_owner', models.CharField(blank=True, max_length=1000, null=True)),
                ('restaurant_phone', models.IntegerField(blank=True, null=True)),
                ('restaurant_addres', models.CharField(blank=True, max_length=10000, null=True)),
                ('restaurant_opentime', models.TimeField(blank=True, null=True)),
                ('restaurant_closetime', models.TimeField(blank=True, null=True)),
                ('restaurant_image', models.CharField(blank=True, max_length=10000, null=True)),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.menu')),
            ],
        ),
    ]
