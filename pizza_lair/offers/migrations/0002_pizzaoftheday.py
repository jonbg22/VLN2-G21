# Generated by Django 4.2.1 on 2023-05-12 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_rename_prodid_drink_prod_rename_prodid_pizza_prod_and_more'),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOfTheDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.SmallIntegerField()),
                ('pizza', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.pizza')),
            ],
        ),
    ]
