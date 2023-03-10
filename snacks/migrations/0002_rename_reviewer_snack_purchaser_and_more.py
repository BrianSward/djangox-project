# Generated by Django 4.1.5 on 2023-01-26 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snack',
            old_name='reviewer',
            new_name='purchaser',
        ),
        migrations.RenameField(
            model_name='snack',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='snack',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='snack',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='snack',
            name='reference_url',
        ),
    ]
