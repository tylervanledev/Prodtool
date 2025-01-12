# Generated by Django 2.1.3 on 2020-02-10 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200213_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureRequestNotificationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_default', models.CharField(default='friend', max_length=255)),
                ('reply_to', models.EmailField(blank=True, max_length=254)),
                ('bcc', models.TextField(blank=True)),
                ('template', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
            ],
        ),
    ]
