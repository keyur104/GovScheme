# Generated by Django 2.2.1 on 2020-07-30 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0013_auto_20200730_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemesgov',
            name='reminstall',
            field=models.IntegerField(default='5'),
            preserve_default=False,
        ),
    ]
