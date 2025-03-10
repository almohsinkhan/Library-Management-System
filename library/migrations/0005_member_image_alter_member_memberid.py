# Generated by Django 5.1.4 on 2025-01-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_member_memberid'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='member',
            name='memberID',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
