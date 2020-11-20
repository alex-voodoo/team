# Generated by Django 3.1.2 on 2020-11-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20201101_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='interest',
            field=models.IntegerField(choices=[(0, 'No interest'), (1, "I wouldn't mind working in this area"), (2, 'I would like to work in this area'), (3, 'I really want to work in this area'), (4, 'I am obsessed with it!')], default=0),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='knowledge',
            field=models.IntegerField(choices=[(0, 'No knowledge'), (1, 'Touched it while doing unrelated things'), (2, 'Did minor things there'), (3, 'Did major things there'), (4, 'Expert')], default=0),
        ),
        migrations.AlterUniqueTogether(
            name='personassessment',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='personassessment',
            constraint=models.UniqueConstraint(fields=('date', 'person'), name='one_assessment_per_day'),
        ),
    ]
