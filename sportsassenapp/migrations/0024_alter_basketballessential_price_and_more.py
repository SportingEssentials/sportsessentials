# Generated by Django 4.2 on 2023-06-15 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsassenapp', '0023_comparison_delete_socceressential_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketballessential',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='comparison',
            name='comp_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
