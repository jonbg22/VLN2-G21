# Generated by Django 4.2.1 on 2023-05-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.CharField(default='/static/images/shoppingcart.svg', max_length=9999),
        ),
    ]