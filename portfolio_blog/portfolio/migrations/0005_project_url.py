# Generated by Django 4.0.5 on 2022-07-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default='placeholder'),
        ),
    ]
