# Generated by Django 4.1.4 on 2022-12-20 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestArticles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]