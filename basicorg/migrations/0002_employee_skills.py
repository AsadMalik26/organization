# Generated by Django 5.1.6 on 2025-03-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicorg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(to='basicorg.skill'),
        ),
    ]
