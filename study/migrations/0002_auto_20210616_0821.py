# Generated by Django 3.0 on 2021-06-16 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-date',)},
        ),
    ]
