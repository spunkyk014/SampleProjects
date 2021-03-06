# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-07 04:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='URLEntry',
            fields=[
                ('url_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('original_url', models.URLField(max_length=300)),
                ('shortened_url', models.URLField()),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
