# Generated by Django 4.0 on 2021-12-17 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=150, null=True, unique=True, verbose_name='Phone Number'),
        ),
    ]
