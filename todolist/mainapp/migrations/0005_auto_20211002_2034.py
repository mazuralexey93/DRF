# Generated by Django 3.1 on 2021-10-02 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210913_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['pk']},
        ),
    ]
