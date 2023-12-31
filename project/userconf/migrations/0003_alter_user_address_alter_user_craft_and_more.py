# Generated by Django 4.2.5 on 2023-09-23 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userconf', '0002_user_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='craft',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gstin',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
