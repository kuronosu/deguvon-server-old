# Generated by Django 2.2.3 on 2019-09-25 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='aid',
            field=models.CharField(max_length=5, unique=True, verbose_name='Anime ID'),
        ),
    ]
