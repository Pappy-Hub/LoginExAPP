# Generated by Django 3.2.7 on 2021-11-03 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Business',
        ),
        migrations.DeleteModel(
            name='Individual',
        ),
    ]