# Generated by Django 4.1.6 on 2023-06-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsassenapp', '0025_rename_comparisons_basketballessential_comparison'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparison',
            name='comp_price_index',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
