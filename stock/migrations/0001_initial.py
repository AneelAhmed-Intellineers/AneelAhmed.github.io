# Generated by Django 2.2.3 on 2019-08-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('ticker', models.CharField(max_length=20)),
                ('shares', models.IntegerField(blank=True, default=None, null=True)),
                ('current_price', models.FloatField(blank=True, default=None, null=True)),
                ('fx_rate', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
