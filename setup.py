#!/usr/bin/env python3
"""First-time setup for School Transport System v2"""
import subprocess, sys

def run(cmd, fatal=True):
    print(f'\n>>> {cmd}')
    rc = subprocess.run(cmd, shell=True).returncode
    if rc != 0 and fatal:
        print(f'ERROR: {cmd}')
        sys.exit(1)
    return rc

print('=' * 55)
print('  نظام النقل المدرسي — الإعداد الأولي  v2')
print('=' * 55)

run(f'"{sys.executable}" -m pip install -r requirements.txt')
run(f'"{sys.executable}" manage.py makemigrations transport')
run(f'"{sys.executable}" manage.py migrate')

print('\n--- إنشاء حساب المدير ---')
print('هذا الحساب يملك صلاحيات كاملة.\n')
run(f'"{sys.executable}" manage.py createsuperuser')

ans = input('\nهل تريد تحميل بيانات تجريبية؟ [y/N] ').strip().lower()
if ans == 'y':
    code = (
        "from transport.models import Driver,LineSupervisor,Student,FamilyContact;"
        "d1=Driver.objects.create(name='أحمد خالد',phone='07801111111',line_number='3');"
        "d2=Driver.objects.create(name='محمد علي',phone='07802222222',line_number='5');"
        "s1=LineSupervisor.objects.create(name='فاطمة حسن',phone='07751111111',line_number='3');"
        "s2=LineSupervisor.objects.create(name='نور محمد',phone='07752222222',line_number='5');"
        "st1=Student.objects.create(name='لينا أحمد',grade='الثالث الابتدائي',area='حي النور',phone1='07701111111',phone2='07702222222',driver=d1,supervisor=s1);"
        "st2=Student.objects.create(name='طارق حسن',grade='الخامس الابتدائي',area='حي السلام',phone1='07703333333',driver=d2,supervisor=s2);"
        "st3=Student.objects.create(name='نورا خالد',grade='الثاني الابتدائي',area='حي الرشيد',phone1='07704444444',driver=d1,supervisor=s1);"
        "FamilyContact.objects.create(student=st1,name='علي أحمد (الأب)',phone='07711111111',order=1);"
        "FamilyContact.objects.create(student=st1,name='هدى حسن (الأم)',phone='07722222222',order=2);"
        "FamilyContact.objects.create(student=st2,name='حسن حسن (الأب)',phone='07733333333',order=1);"
        "FamilyContact.objects.create(student=st3,name='خالد عمر (الأب)',phone='07744444444',order=1);"
        "print('تم تحميل البيانات التجريبية بنجاح!')"
    )
    if run(f'"{sys.executable}" manage.py shell -c "{code}"', fatal=False) != 0:
        print('⚠ فشل تحميل البيانات — يمكنك إضافتها يدوياً')

print('\n' + '=' * 55)
print('  اكتمل الإعداد!')
print('  لتشغيل الخادم:')
print('    python manage.py runserver')
print('  أو للشبكة المحلية:')
print('    python manage.py runserver 0.0.0.0:8000')
print('  الرابط: http://127.0.0.1:8000/')
print('=' * 55)
