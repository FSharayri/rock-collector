# Generated by Django 4.2.16 on 2024-09-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=100)),
                ('size', models.CharField(max_length=30)),
            ],
        ),
    ]
