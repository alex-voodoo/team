# Generated by Django 3.1.2 on 2020-11-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0005_auto_20201102_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
