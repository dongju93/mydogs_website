# Generated by Django 2.2.2 on 2019-07-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20190710_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
