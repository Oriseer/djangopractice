# Generated by Django 3.1.3 on 2020-12-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practiceapp', '0010_auto_20201203_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='img',
            field=models.ImageField(default='media/default_pic.png', upload_to=''),
        ),
    ]
