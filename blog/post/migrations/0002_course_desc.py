# Generated by Django 3.0.6 on 2020-05-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.TextField(default=None, max_length=1000),
        ),
    ]
