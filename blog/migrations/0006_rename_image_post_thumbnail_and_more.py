# Generated by Django 4.1.7 on 2023-07-21 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image_url',
            new_name='thumbnail_url',
        ),
    ]
