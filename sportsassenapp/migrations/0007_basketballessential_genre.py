# Generated by Django 4.1.6 on 2023-05-14 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsassenapp', '0006_basketballessential_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketballessential',
            name='genre',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
