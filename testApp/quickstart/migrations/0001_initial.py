# Generated by Django 2.0.2 on 2018-02-11 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10, verbose_name='Currency ticker')),
                ('name', models.CharField(max_length=10, verbose_name='Currency name')),
                ('priceUSD', models.FloatField(default=-1.0)),
            ],
        ),
    ]
