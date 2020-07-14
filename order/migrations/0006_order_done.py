# Generated by Django 2.2.7 on 2019-12-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_cart_added_key_del'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=300)),
                ('product_price', models.DecimalField(decimal_places=1, max_digits=20)),
                ('product_quantity', models.IntegerField(default=1)),
                ('product_total', models.DecimalField(decimal_places=1, max_digits=20)),
                ('product_size', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
