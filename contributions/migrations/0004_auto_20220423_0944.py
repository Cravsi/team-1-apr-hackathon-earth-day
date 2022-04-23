# Generated by Django 3.2 on 2022-04-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributions', '0003_auto_20220423_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='recycle',
            name='recycle_description',
            field=models.TextField(blank=True, max_length=280, null=True),
        ),
        migrations.AddField(
            model_name='reduce',
            name='reduce_description',
            field=models.TextField(blank=True, max_length=280, null=True),
        ),
        migrations.AddField(
            model_name='reuse',
            name='reuse_description',
            field=models.TextField(blank=True, max_length=280, null=True),
        ),
    ]
