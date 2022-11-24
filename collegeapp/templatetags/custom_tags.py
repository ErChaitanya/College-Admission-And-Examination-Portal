import json
from webbrowser import get
from django import template
from collegeapp.models import *

register = template.Library()

@register.simple_tag
def personal_info(user, data):
    user = User.objects.get(id=user.id)
    try:
        student = Student.objects.get(user=user)
        return getattr(student, data)
    except:
        try:
            return getattr(user, data)
        except:
            return ""


@register.simple_tag
def register_info(user, data):
    user = User.objects.get(id=user.id)
    try:
        student = RegistrationDetail.objects.get(student=user)
        return getattr(student, data)
    except:
        try:
            return getattr(user, data)
        except:
            return ""


@register.simple_tag
def address_info(user, data):
    user = User.objects.get(id=user.id)
    try:
        student = AddressDetail.objects.get(student=user)
        return getattr(student, data)
    except:
        try:
            return getattr(user, data)
        except:
            return ""

@register.simple_tag
def reservation_info(user, data):
    user = User.objects.get(id=user.id)
    try:
        student = ReservationDetail.objects.get(student=user)
        return getattr(student, data)
    except:
        try:
            return getattr(user, data)
        except:
            return ""

@register.simple_tag
def scholarship_info(user, data):
    user = User.objects.get(id=user.id)
    try:
        student = ScholarshipDetail.objects.get(student=user)
        return getattr(student, data)
    except:
        try:
            return getattr(user, data)
        except:
            return ""


@register.simple_tag
def declaration_info(user, data):
    user = User.objects.get(id=user.id)
    try:
        student = DeclarationStudent.objects.get(student=user)
        return getattr(student, data)
    except:
        try:
            return getattr(user, data)
        except:
            return ""

@register.simple_tag
def findsubject(did, data):
    try:
        subject = Subject.objects.get(id=did)
        return getattr(subject, data)
    except:
        return ""

@register.simple_tag
def findsubjectdata(user, data):
    user = User.objects.get(id=user.id)
    try:
        exam = ExaminationProcess.objects.get(student=user)
        subject = (exam.subject).replace("'", '"')
        subject = json.loads(str(subject))
        subject = subject["object"]
        return subject, len(subject)
    except:
        return ""

@register.simple_tag
def finddocdata(user, data):
    user = User.objects.get(id=user.id)
    try:
        exam = ExaminationProcess.objects.get(student=user)
        subject = (exam.previoussem).replace("'", '"')
        subject = json.loads(str(subject))
        subject = subject["object"]
        return subject, len(subject)
    except:
        return ""

@register.simple_tag
def findacademic(user, data):
    user = User.objects.get(id=user.id)
    try:
        academic = AcademicDetail.objects.get(student=user)
        academic = (academic.academics).replace("'", '"')
        academic = json.loads(str(academic))
        academic = academic["object"]
        return academic, len(academic)
    except:
        return ""

@register.simple_tag
def finduploadfile(user, data):
    user = User.objects.get(id=user.id)
    try:
        academic = UploadFileDetail.objects.get(student=user)
        academic = (academic.filename).replace("'", '"')
        academic = json.loads(str(academic))
        academic = academic["object"]
        print(academic)
        return academic, len(academic)
    except:
        return ""