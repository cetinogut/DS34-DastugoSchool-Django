# Generated by Django 3.2.8 on 2021-11-01 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dastugo_school', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mesage',
            new_name='message',
        ),
    ]
