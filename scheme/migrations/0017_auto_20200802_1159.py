# Generated by Django 2.2.1 on 2020-08-02 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0016_auto_20200802_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schemesgov',
            name='docs',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='stateauth',
            name='docs',
            field=models.FileField(upload_to=''),
        ),
    ]