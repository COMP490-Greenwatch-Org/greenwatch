# Generated by Django 3.2.5 on 2022-05-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0006_alter_extendeduser_notification_interval'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='latest_update',
            field=models.DateField(null=True),
        ),
    ]