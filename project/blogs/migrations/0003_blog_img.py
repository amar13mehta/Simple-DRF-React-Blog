# Generated by Django 2.1.9 on 2019-11-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20191113_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='NA', upload_to=''),
            preserve_default=False,
        ),
    ]
