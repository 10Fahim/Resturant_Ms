# Generated by Django 4.2.4 on 2023-10-02 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisine_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Food_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('timing', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('cuisine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RestaurantAPP.cuisine')),
            ],
        ),
    ]