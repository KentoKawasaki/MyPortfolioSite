# Generated by Django 4.0 on 2021-12-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True, null=True, verbose_name='GithubのURL'),
        ),
    ]
