# Generated by Django 2.2.1 on 2020-07-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0009_auto_20200729_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='modify',
            name='ministry',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modify',
            name='sector',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
