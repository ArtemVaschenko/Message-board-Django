# Generated by Django 4.1.7 on 2023-03-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='contact',
            field=models.CharField(default='None', max_length=150, null=True),
        ),
    ]
