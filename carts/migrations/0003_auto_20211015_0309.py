# Generated by Django 3.1 on 2021-10-15 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_varaitions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='varaitions',
            new_name='variation',
        ),
    ]