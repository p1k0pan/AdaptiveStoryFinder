# Generated by Django 4.2 on 2023-06-07 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("wikihow_app", "0004_user_delete_article_delete_person"),
    ]

    operations = [
        migrations.DeleteModel(name="User",),
    ]
