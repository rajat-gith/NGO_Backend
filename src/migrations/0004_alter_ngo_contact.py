# Generated by Django 4.1.1 on 2022-11-11 15:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_ngo_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(default=3, max_length=128, region=None),
            preserve_default=False,
        ),
    ]
