# Generated by Django 5.1.4 on 2025-01-15 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_member_memberid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, default='covers/default_cover.jpg', null=True, upload_to='covers/'),
        ),
        migrations.CreateModel(
            name='BookIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('returned', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member')),
            ],
            options={
                'verbose_name': 'Book Issue',
                'verbose_name_plural': 'Book Issues',
                'db_table': 'book_issues',
                'ordering': ['issue_date'],
            },
        ),
    ]
