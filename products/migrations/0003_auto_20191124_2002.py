# Generated by Django 2.2.7 on 2019-11-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191124_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='size1',
            field=models.CharField(default='Small', max_length=200),
        ),
    ]
