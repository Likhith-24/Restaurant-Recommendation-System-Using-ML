# Generated by Django 4.2.7 on 2023-11-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='order_date',
            field=models.DateField(),
        ),
    ]
