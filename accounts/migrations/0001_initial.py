# Generated by Django 3.2.7 on 2021-10-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phoneNumber', models.IntegerField(default=1)),
                ('referralCode', models.CharField(blank=True, max_length=8, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(default='new', max_length=100)),
                ('email', models.EmailField(default='new', max_length=100)),
                ('phoneNumber', models.IntegerField(default=1)),
                ('referralCode', models.CharField(default='new', max_length=8)),
                ('password', models.CharField(default='new', max_length=50)),
            ],
        ),
    ]
