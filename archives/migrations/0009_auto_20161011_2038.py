# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 12:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('archives', '0008_auto_20161007_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='buyers',
            field=models.ManyToManyField(related_name='user_buy_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_post', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
