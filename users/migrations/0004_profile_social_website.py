# Generated by Django 4.2.10 on 2024-03-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
