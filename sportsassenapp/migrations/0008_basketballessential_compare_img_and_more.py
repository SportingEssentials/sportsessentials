# Generated by Django 4.1.6 on 2023-06-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsassenapp', '0007_basketballessential_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketballessential',
            name='compare_img',
            field=models.ImageField(blank=True, upload_to='basketball_essentials'),
        ),
        migrations.AddField(
            model_name='basketballessential',
            name='compare_name',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]