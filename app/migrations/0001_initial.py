# Generated by Django 4.2.2 on 2023-06-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('response', models.IntegerField(default=2)),
            ],
        ),
    ]
