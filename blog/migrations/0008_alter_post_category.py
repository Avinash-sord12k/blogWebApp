# Generated by Django 4.1.7 on 2023-03-18 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='general', max_length=50),
        ),
    ]
