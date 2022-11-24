from contextlib import nullcontext
from hashlib import blake2b
from secrets import choice
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Semester(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.name

SUBJECTTYPE = ((1, "Core"), (2, "Optional"))
THEORYTYPE = ((1, "Practical"), (2, "Theory"))
class Subject(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    subjecttype = models.IntegerField(choices=SUBJECTTYPE, null=True, blank=True)
    theroytype = models.IntegerField(choices=THEORYTYPE, null=True, blank=True)
    marks = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.name

PASSSTATUS = ((1, 'Unset'), (2, 'Set'))
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    roll_no = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    parent_contact = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    father_name = models.CharField(max_length=200, null=True, blank=True)
    mother_name = models.CharField(max_length=200, null=True, blank=True)
    mother_occupation = models.CharField(max_length=200, null=True, blank=True)
    father_occupation = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    created  = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, null=True)
    dob = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    aadhar_no = models.CharField(max_length=100, null=True, blank=True)
    enrollment_no = models.CharField(max_length=100, null=True, blank=True)
    registration_no = models.CharField(max_length=100, null=True, blank=True)
    passstatus = models.IntegerField(choices=PASSSTATUS, default=1)

    def __str__(self) -> str:
        return self.user.first_name + " . " + self.user.last_name


TYPEOFSEAT = ((1, 'CAP'), (2, 'IL'), (3, 'MINIORITY'), (4, 'j & K'), (5, 'ACAP'), (6, 'TFWS'))
CATEGORY = ((1, 'OPEN'), (2, 'OBC'), (3, 'SC'), (4, 'ST'), (5, 'SBC'), (6, 'ESBC'), (7, 'VJ-DT'), (8, 'NT1'), (9, 'NT2'), (10, 'NT3'), (11, 'EWS'))
RESIDENTIAL_STATUS = ((1, 'MS'), (2, 'OMS'), (3, 'J & K'))
BELONG_TO = ((1, 'URBAN'), (2, 'RURAL'), (3, 'TRIBAL'))
FTAD = ((1, 'FIRST YEAR'), (2, 'DIRECT SECOND YEAR'))
class RegistrationDetail(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    admissionyear = models.CharField(max_length=100, null=True, blank=True)
    seat_type = models.IntegerField(choices=TYPEOFSEAT, default=1, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    category = models.IntegerField(choices=CATEGORY, default=1, null=True, blank=True)
    cap_application_id = models.CharField(max_length=100, null=True, blank=True)
    residential_status = models.IntegerField(choices=RESIDENTIAL_STATUS, default=1, null=True, blank=True)
    belong_to = models.IntegerField(choices=BELONG_TO, null=True, default=1, blank=True)
    ftad = models.IntegerField(choices=FTAD, default=1, null=True, blank=True)
    admission_date = models.DateField(null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=True)
    session = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.student.username



class AddressDetail(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    c_address = models.CharField(max_length=100, null=True, blank=True)
    c_city_vill = models.CharField(max_length=100, null=True, blank=True)
    c_taluka = models.CharField(max_length=100, null=True, blank=True)
    c_district = models.CharField(max_length=100, null=True, blank=True)
    c_state = models.CharField(max_length=100, null=True, blank=True)
    c_pincode = models.CharField(max_length=100, null=True, blank=True)
    p_address = models.CharField(max_length=100, null=True, blank=True)
    p_city_vill = models.CharField(max_length=100, null=True, blank=True)
    p_taluka = models.CharField(max_length=100, null=True, blank=True)
    p_district = models.CharField(max_length=100, null=True, blank=True)
    p_state = models.CharField(max_length=100, null=True, blank=True)
    p_pincode = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.student.username


class ReservationDetail(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    domicile_state = models.CharField(max_length=100, null=True, blank=True)
    caste = models.CharField(max_length=100, null=True, blank=True)
    sub_caste = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.student.username


TYPESCHOLAR = ((1, "Scholarship"), (2, 'Freeship'), (3, 'Minority'), (4, 'EBC'))
class ScholarshipDetail(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    previous_year = models.CharField(max_length=100, null=True, blank=True)
    guardian_profession = models.CharField(max_length=100, null=True, blank=True)
    guardian_income = models.CharField(max_length=100, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    ac_no = models.CharField(max_length=100, null=True, blank=True)
    ifsc = models.CharField(max_length=100, null=True, blank=True)
    micr_code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.student.username


class AcademicDetail(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    academics = models.TextField(null=True, blank=True, default={'class/course':'', 'board':'', 'marks-obtained':'', 'total-marks':'', 'percentage':'', 'SGPA/CGPA':''})

    def __str__(self) -> str:
        return self.student.username


class UploadFileDetail(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    filename = models.TextField(null=True, blank=True, default={'object':[{'filename':'', 'uploadfile':''}]})

    def __str__(self) -> str:
        return self.student.username


class DeclarationStudent(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    sign = models.FileField(null=True, blank=True)
    checked = models.BooleanField(null=True, blank=True)

    def __str__(self) -> str:
        return self.student.username


class ApplyCharge(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=True)
    admissioncharge = models.CharField(max_length=200, null=True, blank=True)
    examcharge = models.CharField(max_length=200, null=True, blank=True)
    created  = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.branch.name +" . "+ self.semester.name


ADMISSIONSTATUS = ((1, 'Pending'), (2, "Verfied"), (3, "Rejected"), (4, 'Payment Pending'), (5, "Payment Completed"))
ADSTATUS = ((1, 'Personal'), (2, "Registartion"), (3, 'Address'), (4, 'Reservation'), (5, 'Scholarship'), (6, 'Academic'), (7, "Upload File"), (8, 'Declaration'), (9, 'Approval'))
class AdmissionProcess(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=ADMISSIONSTATUS, default=1, null=True, blank=True)
    otp = models.CharField(max_length=100, null=True, blank=True)
    adstatus = models.IntegerField(choices=ADSTATUS, default=1, null=True, blank=True)

    def __str__(self) -> str:
        return self.student.first_name +" . "+ self.student.last_name

    
class CommentAdm(models.Model):
    admpro = models.ForeignKey(AdmissionProcess, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=ADMISSIONSTATUS, default=1, null=True, blank=True)

    def __str__(self) -> str:
        return self.admpro.student.first_name +" . "+ self.admpro.student.last_name


EXAMINATIONSTATUS = ((1, 'Pending'), (2, "Verfied"), (3, "Rejected"), (4, 'Payment Pending'), (5, "Payment Completed"))
PAYMENTSTATUS = ((1, 'Pending'), (2, "Completed"))
class ExaminationProcess(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    previoussem = models.TextField(null=True, blank=True)
    signstudent = models.FileField(null=True, blank=True)
    signverifier = models.FileField(null=True, blank=True)
    signhod = models.FileField(null=True, blank=True)
    checkedby = models.FileField(null=True, blank=True)
    student_type = models.CharField(max_length=200, null=True, blank=True)
    dated = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    status = models.IntegerField(choices=EXAMINATIONSTATUS, null=True, blank=True)
    paymentstatus = models.IntegerField(choices=PAYMENTSTATUS, null=True, blank=True)

    def __str__(self) -> str:
        return self.student.first_name +" . "+ self.student.last_name


class CommentExm(models.Model):
    exmpro = models.ForeignKey(ExaminationProcess, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=EXAMINATIONSTATUS, default=1, null=True, blank=True)

    def __str__(self) -> str:
        return self.exmpro.student.first_name +" . "+ self.exmpro.student.last_name


class AttachCard(models.Model):
    exam = models.ForeignKey(ExaminationProcess, on_delete=models.CASCADE, null=True, blank=True)
    attached_card = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.exam.student.first_name +" . "+ self.exam.student.last_name