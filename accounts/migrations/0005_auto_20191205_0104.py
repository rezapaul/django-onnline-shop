# Generated by Django 2.2.7 on 2019-12-04 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191204_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curency',
            name='user_id',
        ),
        migrations.AddField(
            model_name='curency',
            name='user_username',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
