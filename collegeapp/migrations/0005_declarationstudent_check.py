# Generated by Django 3.2.11 on 2022-10-17 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0004_auto_20221017_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='declarationstudent',
            name='check',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
