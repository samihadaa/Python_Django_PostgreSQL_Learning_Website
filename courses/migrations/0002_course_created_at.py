# Generated by Django 4.1.4 on 2022-12-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
