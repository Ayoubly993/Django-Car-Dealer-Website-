# Generated by Django 5.0.3 on 2024-03-26 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_carimage_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='main_car',
            field=models.BooleanField(default=False),
        ),
    ]