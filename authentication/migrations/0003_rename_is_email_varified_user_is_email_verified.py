# Generated by Django 3.2.4 on 2021-08-08 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_is_email_varified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_email_varified',
            new_name='is_email_verified',
        ),
    ]
