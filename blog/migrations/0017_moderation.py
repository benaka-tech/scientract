# Generated by Django 2.1 on 2019-07-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190717_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='moderation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moderation', models.BooleanField(default=False)),
            ],
        ),
    ]