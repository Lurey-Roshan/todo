# Generated by Django 3.2.4 on 2021-07-28 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_varified',
            field=models.BooleanField(default=False),
        ),
    ]
