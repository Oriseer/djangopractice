# Generated by Django 3.1.3 on 2020-11-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0002_auto_20201129_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
