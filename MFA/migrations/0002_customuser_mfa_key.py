# Generated by Django 4.2 on 2023-04-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MFA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mfa_key',
            field=models.CharField(default='', max_length=100),
        ),
    ]
