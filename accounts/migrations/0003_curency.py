# Generated by Django 2.2.7 on 2019-12-04 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('curency', models.IntegerField()),
                ('etebar', models.CharField(blank=True, default=models.IntegerField(), max_length=200)),
            ],
        ),
    ]