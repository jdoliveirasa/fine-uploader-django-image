# Generated by Django 2.0 on 2018-01-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180101_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_csrfmiddlewaretoken',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
