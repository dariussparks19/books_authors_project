# Generated by Django 2.2.4 on 2020-08-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
