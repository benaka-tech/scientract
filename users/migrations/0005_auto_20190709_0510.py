# Generated by Django 2.1 on 2019-07-09 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190709_0432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userclassfication',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='UserClassfication',
            field=models.CharField(blank=True, choices=[('engineers', 'Engineers'), ('doctors', 'Doctors'), ('researchers', 'Researchers'), ('entrepreneur', 'Entrepreneur'), ('academician', 'Academician')], max_length=1, null=True),
        ),
        migrations.DeleteModel(
            name='UserClassfication',
        ),
    ]