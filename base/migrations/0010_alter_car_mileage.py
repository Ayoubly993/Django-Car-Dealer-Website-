# Generated by Django 5.0.3 on 2024-03-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
