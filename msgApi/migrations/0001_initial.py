# Generated by Django 4.1.7 on 2023-03-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=True, null=True)),
                ('day', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
