# Generated by Django 4.2.7 on 2023-12-03 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meerapp', '0006_transaction_executed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='executed',
        ),
    ]