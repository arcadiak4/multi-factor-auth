# Generated by Django 4.1.7 on 2023-04-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, verbose_name='Username')),
                ('password', models.CharField(default='', max_length=100, verbose_name='Password')),
            ],
        ),
    ]