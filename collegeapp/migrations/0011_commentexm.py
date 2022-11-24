# Generated by Django 3.2.11 on 2022-10-25 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0010_examinationprocess_student_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentExm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Pending'), (2, 'Verfied')], default=1, null=True)),
                ('exmpro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.examinationprocess')),
            ],
        ),
    ]