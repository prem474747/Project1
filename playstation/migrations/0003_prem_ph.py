# Generated by Django 4.1.1 on 2022-10-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playstation', '0002_remove_prem_age_remove_prem_gender_prem_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='prem',
            name='ph',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
