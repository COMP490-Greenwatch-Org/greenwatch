# Generated by Django 4.0.3 on 2022-03-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0005_alter_camera_name_alter_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='results',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
