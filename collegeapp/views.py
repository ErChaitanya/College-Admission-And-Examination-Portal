import json
import os
from django.contrib import messages
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import *
import random
import string
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

import string
import secrets
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def student_registration(request, pid=None):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        try:
            user = User.objects.get(username=uname)
            messages.success(request, "Email already exist.")
            return redirect('student_registration')
        except:
            pass
        user = User.objects.create_user(username=uname, password=pwd, first_name=fname, last_name=lname)
        AdmissionProcess.objects.create(student=user)
        messages.success(request, "Registration Successful")
        return redirect('login')
    return render(request, 'student_registration.html', locals()) 


def student_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user:
            login(request,user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentials")
    return render(request, 'login.html', locals()) 


def admin_login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user.is_staff:
            login(request,user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentials")
    return render(request, 'admin_login.html', locals()) 


def complete_registration(request):
    # try:
    #     childcount = AdmissionProcess.objects.get(student=request.user, status__in=[3, 1, 4 , 5])
    #     return redirect('success_page')
    # except:
    #     try:
    #         admdata = AdmissionProcess.objects.get(student=request.user, status=3)
    #         comment = CommentAdm.objects.filter(admpro=admdata)
    #         step = 4
    #     except:
    #         pass
    seat_type = TYPEOFSEAT
    category = CATEGORY
    residential_status = RESIDENTIAL_STATUS
    belong_to = BELONG_TO
    ftad = FTAD
    branch = Branch.objects.all()
    semester = Semester.objects.all()
    admdata = AdmissionProcess.objects.get(student=request.user)
    if admdata.status == 2 or admdata.status == 5:
        return redirect('success_admission')
    comment = CommentAdm.objects.filter(admpro=admdata)
    childcount = admdata.adstatus
    return render(request, 'complete_registration.html', locals()) 


def personal_info(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = Student.objects.get(user=user)
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            new_student = form.save()
            new_student.user = user
            new_student.save()
            if not student:
                childcount.adstatus = 3
                childcount.save()
            # messages.success(request, "Registration Successful")
            response = {
                'child': 2,
                'msg':'Your form has been submitted successfully'
            }
            return JsonResponse(response, status = 200)
        else:
            print(form.errors)
    else:
        print("Hellow World, Else")
    # print("Hellow World")
    response = {
            'child': 2,
            'msg':'Your form has been submitted successfully'
        }
    return JsonResponse(response, status = 200)


def register_info(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = RegistrationDetail.objects.get(student=user)
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            new_student = form.save()
            new_student.student = user
            new_student.save()
            if not student:
                childcount.adstatus = 3
                childcount.save()
            # messages.success(request, "Registration Successful")
            response = {
                'child': 3,
                'msg':'Your form has been submitted successfully'
            }
            return JsonResponse(response, status = 200)
        else:
            print(form.errors)
    response = {
            'child': 3,
            'msg':'Your form has been submitted successfully',
            
        }
    return JsonResponse(response,status = 200)


def addreess_info(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = AddressDetail.objects.get(student=user)
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        form = AddressForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            new_student = form.save()
            new_student.student = user
            new_student.save()
            if not student:
                childcount.adstatus = 4
                childcount.save()
            response = {
                'child': 4,
                'msg':'Your form has been submitted successfully'
            }
            return JsonResponse(response, status = 200)
        else:
            print(form.errors)
    response = {
            'child': 3,
            'msg':'Your form has been submitted successfully',
            
        }
    return JsonResponse(response,status = 200)

def reservation_info(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = ReservationDetail.objects.get(student=user)
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        form = ReservationDetailForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            new_student = form.save()
            new_student.student = user
            new_student.save()
            if not student:
                childcount.adstatus = 5
                childcount.save()
            response = {
                'child': 5,
                'msg':'Your form has been submitted successfully'
            }
            return JsonResponse(response, status = 200)
        else:
            print(form.errors)
    response = {
            'child': 5,
            'msg':'Your form has been submitted successfully',
            
        }
    return JsonResponse(response,status = 200)


def scholarship_info(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = ScholarshipDetail.objects.get(student=user)
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        form = ScholarshipDetailForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            new_student = form.save()
            new_student.student = user
            new_student.save()
            if not student:
                childcount.adstatus = 6
                childcount.save()
            response = {
                'child': 6,
                'msg':'Your form has been submitted successfully'
            }
            return JsonResponse(response, status = 200)
        else:
            print(form.errors)
    response = {
            'child': 6,
            'msg':'Your form has been submitted successfully',
            
        }
    return JsonResponse(response,status = 200)


def academic_info(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = AcademicDetail.objects.get(student=user)
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        total = request.POST['totalform']
        mydict = {"object":[]}
        re = request.POST
        for i in range(1, int(total)+1):
            if re.get('class-'+str(i)):
                mydict["object"].append({"class":re['class-'+str(i)], "board":re['board-'+str(i)], "marks":re['marks-'+str(i)], "total":re['total-'+str(i)], "percentage":re['percentage-'+str(i)], "sgpa":re['sgpa-'+str(i)]})
        if student:
            student.academics = mydict
            student.save()
        else:
            AcademicDetail.objects.create(student=user, academics = mydict)
            if not student:
                childcount.adstatus = 7
                childcount.save()
        response = {
            'child': 7,
            'msg':'Your form has been submitted successfully'
        }
        return JsonResponse(response, status = 200)


def decalartion_info(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = DeclarationStudent.objects.get(student=user)
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        form = DeclarationStudentFORM(request.POST, request.FILES, instance=student)
        if form.is_valid():
            new_student = form.save()
            new_student.student = user
            new_student.save()
            if not student:
                childcount.adstatus = 9
                childcount.save()
            response = {
                'child': 9,
                'msg':'Your form has been submitted successfully'
            }
            return JsonResponse(response, status = 200)
        else:
            print(form.errors)
    response = {
            'child': 9,
            'msg':'Your form has been submitted successfully',
            
        }
    return JsonResponse(response,status = 200)

def filesavemedia(file):
    upload_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
    rel_path = os.path.join(datetime.now().strftime('%Y%m%d'), upload_id)
    fs = FileSystemStorage(location=os.path.join(str(settings.MEDIA_ROOT), rel_path))
    fs.save(file.name, file)
    return rel_path+"/"+file.name


def uploadfile_info(request):
    user = User.objects.get(id=request.user.id)
    studentdict= []
    try:
        student = UploadFileDetail.objects.get(student=user)
        studentdict = (student.filename).replace("'", '"')
        studentdict = json.loads(str(studentdict))
        studentdict = studentdict["object"]
    except:
        student = None
    childcount = AdmissionProcess.objects.get(student=request.user)
    if request.method == "POST":
        req = request.POST
        ref = request.FILES
        mydict = {"object":[]}
        total = req['totalform']
       
        for i in range(1, int(total)+1):
            if req.get('filename-'+str(i)):
                if student and len(studentdict) >= i:
                    try:
                        file = ref['certificate-'+str(i)]
                        studentdict[i-1]['certificate'] = filesavemedia(file)
                        studentdict[i-1]['filename'] = req['filename-'+str(i)]
                    except:
                        studentdict[i-1]['filename'] = req['filename-'+str(i)]
                elif student and len(studentdict) < i:
                    try:
                        file = ref['certificate-'+str(i)]
                        studentdict.append({"filename":req['filename-'+str(i)], "certificate":filesavemedia(file)})
                    except:
                        studentdict.append({"filename":req['filename-'+str(i)], "certificate":''})
                else:
                    mydict['object'].append({"filename":req['filename-'+str(i)], "certificate":filesavemedia(ref['certificate-'+str(i)])})

        if student:
            UploadFileDetail.objects.filter(id=student.id).update(filename={"object":studentdict})
        else:
            UploadFileDetail.objects.create(student=request.user, filename=mydict)
            childcount.adstatus = 8
            childcount.save()
        response = {
                'child': 8,
                'msg':'Your form has been submitted successfully'
            }
        return JsonResponse(response, status = 200)
                
        


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('home')


def admission_data(request):
    status = request.GET.get('status')
    branch = Branch.objects.all()
    student = RegistrationDetail.objects.filter()
    admissiondata = AdmissionProcess.objects.filter(status=status)
    admid = [i.student.id for i in admissiondata]
    student = student.filter(student__id__in=admid)
    if request.GET.get('type') == 'table':
        return render(request, "admission_data_table.html", locals())
    return render(request, "admission_data.html", locals())


def admission_data_detail(request, pid):
    user = User.objects.get(id=pid)
    student = Student.objects.get(user=user)
    register = RegistrationDetail.objects.get(student=user)
    address = AddressDetail.objects.get(student=user)
    reserve = ReservationDetail.objects.get(student=user)
    scholar = ScholarshipDetail.objects.get(student=user)
    academic = AcademicDetail.objects.get(student=user)
    declare = DeclarationStudent.objects.get(student=user)
    approveform = AdmissionProcess.objects.get(student=user)
    approveco = CommentAdm.objects.filter(admpro=approveform)
    if request.method == "POST":
        st = request.POST['status']
        co = request.POST['comment']
        approveform.status = st
        approveform.comment = co
        approveform.save()
        CommentAdm.objects.create(admpro = approveform, status=st, comment=co)
        messages.success(request, "Post successfully")
        return redirect('admission_data_detail', pid)
    academic = (academic.academics).replace("'", '"')
    academic = json.loads(str(academic))
    academic = academic["object"]
    studentall = Student.objects.filter().exclude(user=user)
    adstatus = ADSTATUS
    admstatus = ADMISSIONSTATUS
    lendata = len(adstatus)
    return render(request, "admission_data_detail.html", locals())

def success_admission(request):
    user = User.objects.get(id=request.user.id)
    student = Student.objects.get(user=user)
    register = RegistrationDetail.objects.get(student=user)
    address = AddressDetail.objects.get(student=user)
    reserve = ReservationDetail.objects.get(student=user)
    scholar = ScholarshipDetail.objects.get(student=user)
    academic = AcademicDetail.objects.get(student=user)
    declare = DeclarationStudent.objects.get(student=user)
    approveform = AdmissionProcess.objects.get(student=user)
    approveco = CommentAdm.objects.filter(admpro=approveform)
    academic = (academic.academics).replace("'", '"')
    academic = json.loads(str(academic))
    academic = academic["object"]
    # studentall = Student.objects.filter().exclude(user=user)
    adstatus = ADSTATUS
    admstatus = ADMISSIONSTATUS
    lendata = len(adstatus)
    return render(request, "success_admission.html", locals())

def examination_data(request):
    status = request.GET.get('status')
    branch = Branch.objects.all()
    student = RegistrationDetail.objects.filter()
    examdata = ExaminationProcess.objects.filter(status=status)
    examid = [i.student.id for i in examdata]
    student = student.filter(student__id__in=examid)
    if request.GET.get('type') == 'table':
        return render(request, "exam_data_table.html", locals())
    return render(request, "examination_data.html", locals())


def exam_data_detail(request, pid):
    user = User.objects.get(id=pid)
    student = Student.objects.get(user=user)
    register = RegistrationDetail.objects.get(student=user)
    address = AddressDetail.objects.get(student=user)
    data = ExaminationProcess.objects.get(student=user)
    approveco = CommentExm.objects.filter(exmpro=data)
    if request.method == "POST":
        st = request.POST['status']
        co = request.POST['comment']
        data.status = st
        data.comment = co
        data.save()
        CommentExm.objects.create(exmpro=data, status=st, comment=co)
        messages.success(request, "Post successfully")
        return redirect('exam_data_detail', pid)
    course = None
    if data.subject:
        course = (data.subject).replace("'", '"')
        course = json.loads(str(course))
        course = course['object']
    info = None
    if data.previoussem:
        info = (data.previoussem).replace("'", '"')
        info = json.loads(str(info))
        info = info["object"]
    studentall = Student.objects.filter().exclude(user=user)
    admstatus = EXAMINATIONSTATUS
    return render(request, "exam_data_detail.html", locals())


def success_page(request):
    user = User.objects.get(id=request.user.id)
    exam = ExaminationProcess.objects.get(student=user)
    return render(request, "success_page.html", locals())


def payment(request):
    action = request.GET.get('action')
    if request.method == "POST":
        if action:
            adm = AdmissionProcess.objects.get(student=request.user)
            adm.status = 5
            adm.save()
            comment = CommentAdm.objects.create(status=5, comment="Auto created by user", admpro=adm)
            messages.success(request, "Payment Successful")
            return redirect('success_admission')
        else:
            exam = ExaminationProcess.objects.get(student=request.user)
            exam.status = 5
            exam.save()
            comment = CommentExm.objects.create(status=5, comment="Auto created by user", exmpro=exam)
            messages.success(request, "Payment Successful")
            return redirect('success_page')
        
    return render(request, "payment.html", locals())


def invoice(request):
    student = Student.objects.get(user=request.user)
    return render(request, "invoice.html", locals())


def exam_process(request, step=1):
    user = User.objects.get(id=request.user.id)
    try:
        mainstu = RegistrationDetail.objects.get(student=user)
    except:
        messages.success(request, "You need to admission first")
        return redirect('home')
    try:
        childcount = ExaminationProcess.objects.get(student=request.user, status__in=[2, 1, 4 , 5])
        return redirect('success_page')
    except:
        try:
            exmdata = ExaminationProcess.objects.get(student=request.user, status=3)
            comment = CommentExm.objects.filter(exmpro=exmdata)
            step = 4
        except:
            pass
    myexmdata = ExaminationProcess.objects.filter(student=request.user)
    if request.method == "POST":
        total = request.POST['totalform']
        totaldoc = request.POST['totaldocform']
        mysub = {"object":[]}
        re = request.POST
        for i in range(1, int(total)+1):
            if re.get('subject-'+str(i)):
                mysub["object"].append({"subject":re['subject-'+str(i)]})
        
        mydoc = {"object":[]}
        for i in range(1, int(totaldoc)+1):
            if re.get('sem-'+str(i)):
                mydoc["object"].append({"semester":re['sem-'+str(i)], "exam":re['exam-'+str(i)], "credit":re['credit-'+str(i)], "result":re['result-'+str(i)], "sgpa":re['sgpa-'+str(i)]})
        if not myexmdata:
            exam = ExaminationProcess.objects.create(student=user,student_type=re['typestudent'], subject=mysub, previoussem=mydoc)
            exam.status = 1
            exam.save()
        else:
            exam = ExaminationProcess.objects.filter(id=myexmdata.first().id).update(student=user,student_type=re['typestudent'], subject=mysub, previoussem=mydoc, status = 1)
        student = Student.objects.filter(user=user).update(contact=re["contact"])
        stu = Student.objects.get(user=user)
        print("Bhuwan is the best.")
        try:
            stu.image= request.FILES['image']
            stu.save()
        except:
            pass
        add = AddressDetail.objects.filter(student=user).update(c_address=re["address"])
        for i in range(1, int(totaldoc)+1):
            try:
                AttachCard.objects.create(exam=exam, attached_card=request.FILES['upload-'+str(i)])
            except:
                pass
        response = {
            'msg':'Your form has been submitted successfully'
        }
        return JsonResponse(response, status = 200)
    course = Subject.objects.filter(branch=mainstu.branch,semester=mainstu.semester)
    return render(request, "exam_process.html", locals())

def getpractical_marks(request):
    sid = request.GET.get('subjectid')
    course = Subject.objects.get(id=sid)
    theory = ""
    for i in THEORYTYPE:
        if i[0] == course.theroytype:
            theory = i[1]
    
    dic = {'practical':theory, 'marks':course.marks}
    return JsonResponse(dic, status = 200)


def change_branch(request, pid=None):
    branch = None
    if pid:
        branch = Branch.objects.get(id=pid)
    if request.method == "POST":
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            newbr = form.save()
            if pid:
                messages.success(request, "Branch updated")
            else:
                messages.success(request, "Branch added")
            return redirect('manage_branch')
    return render(request, 'change_branch.html', locals())

def manage_branch(request):
    branch = Branch.objects.all()
    return render(request, 'manage_branch.html', locals())

def delete_branch(request, pid):
    branch = Branch.objects.get(id=pid)
    branch.delete()
    messages.success(request, "Branch deleted")
    return redirect('manage_branch')


def change_semester(request, pid=None):
    semester = None
    if pid:
        semester = Semester.objects.get(id=pid)
    if request.method == "POST":
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            newbr = form.save()
            if pid:
                messages.success(request, "Semester updated")
            else:
                messages.success(request, "Semester added")
            return redirect('manage_semester')
    return render(request, 'change_semester.html', locals())

def manage_semester(request):
    semester = Semester.objects.all()
    return render(request, 'manage_semester.html', locals())

def delete_semester(request, pid):
    semester = Semester.objects.get(id=pid)
    semester.delete()
    messages.success(request, "Semester deleted")
    return redirect('manage_semester')


def change_subject(request, pid=None):
    branch = None
    if pid:
        subject = Subject.objects.get(id=pid)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            newbr = form.save()
            if pid:
                messages.success(request, "Subject updated")
            else:
                messages.success(request, "Subject added")
            return redirect('manage_subject')
    semester = Semester.objects.all()
    branch = Branch.objects.all()
    theroytype = THEORYTYPE
    subjecttype = SUBJECTTYPE
    return render(request, 'change_subject.html', locals())

def manage_subject(request):
    subject = Subject.objects.all()
    return render(request, 'manage_subject.html', locals())

def delete_subject(request, pid):
    subject = Subject.objects.get(id=pid)
    subject.delete()
    messages.success(request, "Subject deleted")
    return redirect('manage_subject')


def sendmail(sender, toemail, toname, fromemail, subject, message):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = subject
    html_content = message
    sender = {"name": sender, "email": fromemail}
    to = [{"email": toemail, "name": toname}]
    headers = {"Some-Custom-Name": "unique-id-1234"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers,html_content=html_content, sender=sender, subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


def genratePassword():
    digits = string.digits
    alphabet = digits
    pwd_length = 6
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    return pwd


def sendemail(request):
    req = request.POST
    try:
        user = User.objects.get(username=req['email'])
        userprofile = AdmissionProcess.objects.get(student=user)
    except:
        return JsonResponse({'id':2,'msg':"Invalid Email"})
    pwd = genratePassword()
    userprofile.otp = pwd
    userprofile.save()
    sendmail("College System", req['email'], user.first_name+" "+user.last_name, 'arshansari045@gmail.com', "Forgot Password", "Hi "+user.first_name+" "+user.last_name+", Your OTP is "+pwd)
    return JsonResponse({'id':1, 'msg':"Email send sucessful"})


def checkotp(request):
    req = request.POST

    try:
        user = User.objects.get(username=req['email'])
        userprofile = AdmissionProcess.objects.get(student=user)
    except:
        pass
    if userprofile.otp == req['otp']:
        return JsonResponse({'id':1 ,'msg':"OTP matched successfully"})
    else:
        return JsonResponse({'id':2, 'msg':"Invalid OTP"})

def forgot_password(request):
    if request.method == 'POST':
        n = request.POST.get('new')
        user = User.objects.get(username=request.POST['email'])
        user.set_password(n)
        user.save()
        messages.success(request, "Password Changed")
        return redirect('login')
    return render(request, 'forgot_passowrd.html')

