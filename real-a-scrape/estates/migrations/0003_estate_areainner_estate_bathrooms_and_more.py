# Generated by Django 4.2.5 on 2023-09-17 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estates', '0002_rename_drink_estate'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='AreaInner',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AddField(
            model_name='estate',
            name='Bathrooms',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AddField(
            model_name='estate',
            name='BedroomsInner',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AddField(
            model_name='estate',
            name='Image',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='estate',
            name='Location',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='estate',
            name='Price',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='estate',
            name='Title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
