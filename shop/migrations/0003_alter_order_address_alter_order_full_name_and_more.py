# Generated by Django 5.1.4 on 2024-12-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_address_order_full_name_order_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='for example: karaj, gohardasht...', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='for example: arash eyvazkhani', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='for example: 09122222222', max_length=15),
        ),
    ]