# Generated by Django 4.1.2 on 2022-11-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='reminder_time',
        ),
        migrations.AddField(
            model_name='reminder',
            name='showing_dete',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]