# Generated by Django 3.0.4 on 2020-04-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200423_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='displayimage',
            field=models.ImageField(null=True, upload_to='', verbose_name=''),
        ),
    ]
