# Generated by Django 3.0.4 on 2020-04-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0008_auto_20200426_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wcomment',
            name='body',
            field=models.TextField(blank=True, default='nice', max_length=140),
        ),
    ]
