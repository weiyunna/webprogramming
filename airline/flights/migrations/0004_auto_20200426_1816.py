# Generated by Django 3.0.3 on 2020-04-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_auto_20200426_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]