# Generated by Django 2.2.7 on 2019-11-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='card_token',
            field=models.TextField(),
        ),
    ]