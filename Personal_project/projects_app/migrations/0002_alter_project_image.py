# Generated by Django 5.1.3 on 2024-11-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]