# Generated by Django 4.2 on 2024-06-01 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_upload_username_alter_upload_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='branch',
            field=models.CharField(default='0', max_length=10),
        ),
    ]