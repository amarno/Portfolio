# Generated by Django 2.2.6 on 2019-10-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testStore', '0004_product_photo1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
