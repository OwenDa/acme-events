# Generated by Django 4.1.2 on 2022-10-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_event_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='featured_image',
            field=models.ImageField(blank=True, default='placeholder_anvil_9KRsiCg.jpeg', null=True, upload_to='event_images'),
        ),
    ]
