# Generated by Django 3.2.6 on 2021-10-04 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0002_hero_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='age',
        ),
    ]
