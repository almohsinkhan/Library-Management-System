# Generated by Django 5.1.4 on 2025-01-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_book_cover_bookissue'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='No_of_copies_issued',
            field=models.IntegerField(default=0),
        ),
    ]
