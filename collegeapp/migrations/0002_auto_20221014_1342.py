# Generated by Django 3.2.11 on 2022-10-14 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='session',
        ),
        migrations.AddField(
            model_name='student',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='enrollment_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='registration_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ScholarshipDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('previous_year', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_profession', models.CharField(blank=True, max_length=100, null=True)),
                ('guardian_income', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ac_no', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc', models.CharField(blank=True, max_length=100, null=True)),
                ('micr_code', models.CharField(blank=True, max_length=100, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domicile_state', models.CharField(blank=True, max_length=100, null=True)),
                ('caste', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_caste', models.CharField(blank=True, max_length=100, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionyear', models.CharField(blank=True, max_length=100, null=True)),
                ('seat_type', models.IntegerField(blank=True, choices=[(1, 'CAP'), (2, 'IL'), (3, 'MINIORITY'), (4, 'j & K'), (5, 'ACAP'), (6, 'TFWS')], null=True)),
                ('category', models.IntegerField(blank=True, choices=[(1, 'OPEN'), (2, 'OBC'), (3, 'SC'), (4, 'ST'), (5, 'SBC'), (6, 'ESBC'), (7, 'VJ-DT'), (8, 'NT1'), (9, 'NT2'), (10, 'NT3'), (11, 'EWS')], null=True)),
                ('cap_application_id', models.CharField(blank=True, max_length=100, null=True)),
                ('residential_status', models.IntegerField(blank=True, choices=[(1, 'MS'), (2, 'OMS'), (3, 'J & K')], null=True)),
                ('belong_to', models.IntegerField(blank=True, choices=[(1, 'URBAN'), (2, 'RURAL'), (3, 'TRIBAL')], null=True)),
                ('ftad', models.IntegerField(blank=True, choices=[(1, 'FIRST YEAR'), (2, 'DIRECT SECOND YEAR')], null=True)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('session', models.CharField(blank=True, max_length=200, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.branch')),
                ('semester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.semester')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='DeclarationStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('sign', models.FileField(blank=True, null=True, upload_to='')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='AddressDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_address', models.CharField(blank=True, max_length=100, null=True)),
                ('c_city_vill', models.CharField(blank=True, max_length=100, null=True)),
                ('c_taluka', models.CharField(blank=True, max_length=100, null=True)),
                ('c_district', models.CharField(blank=True, max_length=100, null=True)),
                ('c_state', models.CharField(blank=True, max_length=100, null=True)),
                ('c_pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('p_address', models.CharField(blank=True, max_length=100, null=True)),
                ('p_city_vill', models.CharField(blank=True, max_length=100, null=True)),
                ('p_taluka', models.CharField(blank=True, max_length=100, null=True)),
                ('p_district', models.CharField(blank=True, max_length=100, null=True)),
                ('p_state', models.CharField(blank=True, max_length=100, null=True)),
                ('p_pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.student')),
            ],
        ),
        migrations.CreateModel(
            name='AcademicDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academics', models.TextField(blank=True, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collegeapp.student')),
            ],
        ),
    ]