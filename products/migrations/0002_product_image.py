# Generated by Django 4.2.4 on 2023-08-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]