# Generated by Django 3.1 on 2021-10-15 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20211015_0309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
    ]