# Generated by Django 3.2.7 on 2021-11-07 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LogExAPP', '0004_alter_business_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='fullname',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='phoneNumber',
            new_name='phonen_number',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='referralCode',
            new_name='referral_Code',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='username',
            new_name='user_name',
        ),
    ]