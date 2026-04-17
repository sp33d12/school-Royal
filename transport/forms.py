from django import forms
from django.contrib.auth.models import User
from .models import Driver, LineSupervisor, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'grade', 'area', 'landmark', 'phone1', 'phone2', 'driver', 'supervisor', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'اسم التلميذ'}),
            'grade': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'المرحلة الدراسية'}),
            'area': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'منطقة السكن'}),
            'landmark': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'مثال: مقابل جامع الرحمن'}),
            'phone1': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'هاتف 1'}),
            'phone2': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'هاتف 2'}),
            'driver': forms.Select(attrs={'class': 'field-input'}),
            'supervisor': forms.Select(attrs={'class': 'field-input'}),
            'notes': forms.Textarea(attrs={'class': 'field-input', 'rows': 2, 'placeholder': 'ملاحظات (اختياري)'}),
        }


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'phone', 'line_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'اسم السائق'}),
            'phone': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'رقم الهاتف'}),
            'line_number': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'رقم الخط'}),
        }


class LineSupervisorForm(forms.ModelForm):
    class Meta:
        model = LineSupervisor
        fields = ['name', 'phone', 'line_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'اسم المسؤولة'}),
            'phone': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'رقم الهاتف'}),
            'line_number': forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'رقم الخط'}),
        }


class EmployeeForm(forms.Form):
    username = forms.CharField(
        max_length=150, label='اسم المستخدم',
        widget=forms.TextInput(attrs={'class': 'field-input', 'placeholder': 'اسم المستخدم'})
    )
    password = forms.CharField(
        label='كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'field-input', 'placeholder': 'كلمة المرور'})
    )
    password2 = forms.CharField(
        label='تأكيد كلمة المرور',
        widget=forms.PasswordInput(attrs={'class': 'field-input', 'placeholder': 'تأكيد كلمة المرور'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('اسم المستخدم موجود مسبقاً')
        return username

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('كلمتا المرور غير متطابقتين')
        return cleaned_data
