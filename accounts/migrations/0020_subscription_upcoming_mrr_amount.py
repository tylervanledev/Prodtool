# Generated by Django 2.1.3 on 2020-03-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200326_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='upcoming_mrr_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]