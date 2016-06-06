# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('poisManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poisManage.POI')),
            ],
        ),
        migrations.CreateModel(
            name='data_user',
            fields=[
                ('uid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('city', models.IntegerField(blank=True, default=0)),
                ('province', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poisManage.POI')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poisRecommend.data_user')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poisManage.POI')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poisRecommend.data_user')),
            ],
        ),
        migrations.AddField(
            model_name='check',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poisRecommend.data_user'),
        ),
    ]
