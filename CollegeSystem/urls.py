from turtle import settiltangle
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from collegeapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),

    path('login/', student_login, name='login'),
    path('admin-login/', admin_login, name='admin_login'),
    path('logout/', logout_user, name='logout_user'),
    
    path('student-register/', student_registration, name='student_registration'),
    path('complete-registration/', complete_registration, name='complete_registration'),
    path('personal-info', personal_info, name='personal_info'),
    path('register-info', register_info, name='register_info'),
    path('addreess-info', addreess_info, name='addreess_info'),
    path('reservation-info', reservation_info, name='reservation_info'),
    path('scholarship-info', scholarship_info, name='scholarship_info'),
    path('academic-info', academic_info, name='academic_info'),
    path('decalartion-info', decalartion_info, name='decalartion_info'),
    path('uploadfile-info', uploadfile_info, name='uploadfile_info'),


    path('admission-data/', admission_data, name='admission_data'),
    path('success-admission/', success_admission, name='success_admission'),
    path('admission-data-detail/<int:pid>/', admission_data_detail, name='admission_data_detail'),


    path('exam-process/', exam_process, name='exam_process'),
    path('exam-process-steps/<int:pid>/', exam_process, name='exam_process_steps'),
    path('getpractical-marks/', getpractical_marks, name='getpractical_marks'),
    path('success_page/', success_page, name='success_page'),
    path('payment/', payment, name='payment'),
    path('invoice/', invoice, name='invoice'),

    path('examination-data/', examination_data, name='examination_data'),
    path('exam-data-detail/<int:pid>/', exam_data_detail, name='exam_data_detail'),


    path('add-branch/', change_branch, name='add_branch'),
    path('manage-branch/', manage_branch, name='manage_branch'),
    path('change-branch/<int:pid>/', change_branch, name='change_branch'),
    path('delete-branch/<int:pid>/', delete_branch, name='delete_branch'),

    path('add-semester/', change_semester, name='add_semester'),
    path('manage-semester/', manage_semester, name='manage_semester'),
    path('change-semester/<int:pid>/', change_semester, name='change_semester'),
    path('delete-semester/<int:pid>/', delete_semester, name='delete_semester'),

    path('add-subject/', change_subject, name='add_subject'),
    path('manage-subject/', manage_subject, name='manage_subject'),
    path('change-subject/<int:pid>/', change_subject, name='change_subject'),
    path('delete-subject/<int:pid>/', delete_subject, name='delete_subject'),

    path('sendemail/', sendemail, name='sendemail'),
    path('sendotp/', checkotp, name='sendotp'),
    path('forgot-password/', forgot_password, name='forgot_password'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "SBJain Admin Login"
admin.site.site_title = "Admission and Examination System"
admin.site.index_title = "Welcome to SBJain Admission and Examination Portal"