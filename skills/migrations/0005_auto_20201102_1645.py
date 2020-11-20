# Generated by Django 3.1.2 on 2020-11-02 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0004_auto_20201102_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='personassessment',
            name='latest',
            field=models.BooleanField(default=False),
        ),
        migrations.AddConstraint(
            model_name='personassessment',
            constraint=models.UniqueConstraint(condition=models.Q(latest=True), fields=('person',), name='one_latest_per_person'),
        ),
    ]
