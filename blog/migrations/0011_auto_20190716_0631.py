# Generated by Django 2.1 on 2019-07-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190716_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='document',
            field=models.FileField(blank=True, default='', null=True, upload_to='documents/'),
        ),
    ]
