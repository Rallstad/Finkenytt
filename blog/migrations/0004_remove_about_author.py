# Generated by Django 4.0.2 on 2023-02-03 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_about_options_alter_about_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='author',
        ),
    ]