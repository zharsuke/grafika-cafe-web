# Generated by Django 4.0.4 on 2022-05-26 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pos', '0003_salesitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesitem',
            name='user',
        ),
        migrations.AddField(
            model_name='sales',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
