# Generated by Django 4.1.3 on 2022-11-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_auto_20210502_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='last_change',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='last_success',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
