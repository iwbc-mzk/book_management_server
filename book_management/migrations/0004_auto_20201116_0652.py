# Generated by Django 3.1.3 on 2020-11-15 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0003_auto_20201116_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='label',
            old_name='publisher_id',
            new_name='publisher',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='author_id',
            new_name='author',
        ),
    ]
