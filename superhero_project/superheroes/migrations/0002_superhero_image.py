# Generated by Django 3.2.7 on 2021-11-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='superhero_images/'),
        ),
    ]