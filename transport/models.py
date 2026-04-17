from django.db import models
from django.core.exceptions import ValidationError


class Driver(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم السائق')
    phone = models.CharField(max_length=30, verbose_name='رقم الهاتف')
    line_number = models.CharField(max_length=20, blank=True, verbose_name='رقم الخط')

    def __str__(self):
        line = f' — خط {self.line_number}' if self.line_number else ''
        return f'{self.name}{line}'

    class Meta:
        ordering = ['name']
        verbose_name = 'سائق'
        verbose_name_plural = 'السائقون'


class LineSupervisor(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم المسؤولة')
    phone = models.CharField(max_length=30, verbose_name='رقم الهاتف')
    line_number = models.CharField(max_length=20, blank=True, verbose_name='رقم الخط')

    def __str__(self):
        line = f' — خط {self.line_number}' if self.line_number else ''
        return f'{self.name}{line}'

    class Meta:
        ordering = ['name']
        verbose_name = 'مسؤولة خط'
        verbose_name_plural = 'مسؤولات الخطوط'


class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name='اسم التلميذ')
    grade = models.CharField(max_length=50, verbose_name='المرحلة')
    area = models.CharField(max_length=150, blank=True, verbose_name='منطقة السكن')
    landmark = models.CharField(max_length=200, blank=True, verbose_name='نقطة دالة')
    phone1 = models.CharField(max_length=30, blank=True, verbose_name='هاتف 1')
    phone2 = models.CharField(max_length=30, blank=True, verbose_name='هاتف 2')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='students', verbose_name='السائق')
    supervisor = models.ForeignKey(LineSupervisor, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='students', verbose_name='مسؤولة الخط')
    photo = models.ImageField(upload_to='students/', null=True, blank=True, verbose_name='الصورة')
    notes = models.TextField(blank=True, verbose_name='ملاحظات')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'تلميذ'
        verbose_name_plural = 'التلاميذ'


class FamilyContact(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=150, verbose_name='الاسم')
    phone = models.CharField(max_length=30, blank=True, verbose_name='الهاتف')
    order = models.PositiveSmallIntegerField(default=1, verbose_name='الترتيب')

    def __str__(self):
        return f'{self.name} ({self.student.name})'

    class Meta:
        ordering = ['order']
        verbose_name = 'مخوّل'
        verbose_name_plural = 'المخوّلون'
