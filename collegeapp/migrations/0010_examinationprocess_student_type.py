# Generated by Django 3.2.11 on 2022-10-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0009_auto_20221021_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinationprocess',
            name='student_type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
