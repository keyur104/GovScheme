# Generated by Django 2.2.1 on 2020-07-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheme', '0008_schemesgov_rejreason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme', models.CharField(max_length=500)),
                ('provisions', models.TextField()),
                ('funds', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Centralgov',
        ),
        migrations.AlterField(
            model_name='schemesgov',
            name='rejreason',
            field=models.TextField(),
        ),
    ]