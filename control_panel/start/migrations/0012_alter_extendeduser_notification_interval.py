# Generated by Django 3.2.5 on 2022-05-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0011_merge_20220506_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='notification_interval',
            field=models.CharField(choices=[('immediate', 'Immediately'), ('daily', 'Daily'), ('weekly', 'Weekly')], default='weekly', max_length=11),
        ),
    ]
