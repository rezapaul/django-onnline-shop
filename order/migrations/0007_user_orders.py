# Generated by Django 2.2.7 on 2019-12-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
