# Generated by Django 5.1.4 on 2024-12-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='No address provided', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='full_name',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='000000000000', max_length=15),
        ),
    ]
