# Generated by Django 2.1 on 2019-07-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/group_pics'),
        ),
    ]
