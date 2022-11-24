from dataclasses import field
from pyexpat import model
from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = ('id', 'first_name', 'last_name', 'username', 'password')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'roll_no', 'contact', 'parent_contact', 'gender', 'state', 'city', 'father_name', 'mother_name', 'mother_occupation', 'father_occupation', 'address','nationality', 'aadhar_no', 'enrollment_no', 'registration_no', 'image', 'dob')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationDetail
        fields = ('id', 'admissionyear','branch', 'category',  'semester', 'session',  'admission_date', 'ftad', 'belong_to',  'residential_status', 'cap_application_id', 'seat_type',)

class ScholarshipDetailForm(forms.ModelForm):
    class Meta:
        model = ScholarshipDetail
        fields = ('id', 'type','previous_year', 'branch', 'guardian_profession', 'guardian_income', 'bank_name', 'ac_no', 'ifsc', 'micr_code')

class ReservationDetailForm(forms.ModelForm):
    class Meta:
        model = ReservationDetail
        fields = ('id', 'sub_caste','caste', 'domicile_state')

class AcademicDetailForm(forms.ModelForm):
    class Meta:
        model = AcademicDetail
        fields = ('id', 'academics')

class DeclarationStudentFORM(forms.ModelForm):
    class Meta:
        model = DeclarationStudent
        fields = ('id', 'date', 'place', 'sign', 'checked')


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressDetail
        fields = ('id', 'c_address','c_city_vill', 'c_taluka',  'c_district', 'c_state',  'c_pincode', 'p_address', 'p_city_vill',  'p_taluka', 'p_district', 'p_state', 'p_pincode')


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ('id', 'name', 'code',)


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('id', 'name',)


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'code', 'semester', 'branch', 'subjecttype')


class ApplyChargeForm(forms.ModelForm):
    class Meta:
        model = ApplyCharge
        fields = ('id', 'admissioncharge', 'examcharge', 'semester', 'branch')


class ApplyChargeForm(forms.ModelForm):
    class Meta:
        model = ApplyCharge
        fields = ('id', 'admissioncharge', 'examcharge', 'semester', 'branch')


class AdmissionProcessForm(forms.ModelForm):
    class Meta:
        model = AdmissionProcess
        fields = ('id', 'student', 'status')


class ExaminationForm(forms.ModelForm):
    class Meta:
        model = ExaminationProcess
        fields = ('id', 'student', 'status', 'subject', 'paymentstatus')