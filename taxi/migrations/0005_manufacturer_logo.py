# Generated by Django 4.0.2 on 2022-08-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='logo',
            field=models.ImageField(default=1, upload_to='media/logos'),
            preserve_default=False,
        ),
    ]