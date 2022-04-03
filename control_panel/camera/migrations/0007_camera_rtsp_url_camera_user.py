# Generated by Django 4.0.3 on 2022-03-30 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camera', '0006_image_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='rtsp_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='camera',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
