# Generated by Django 2.1 on 2019-07-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20190706_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='group_pics'),
        ),
    ]
