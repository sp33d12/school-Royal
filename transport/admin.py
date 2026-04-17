from django.contrib import admin
from .models import Driver, LineSupervisor, Student, FamilyContact

class FamilyContactInline(admin.TabularInline):
    model = FamilyContact
    extra = 1
    max_num = 6

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'line_number')
    search_fields = ('name',)

@admin.register(LineSupervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'line_number')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'area', 'landmark', 'driver', 'supervisor')
    search_fields = ('name', 'grade', 'area', 'landmark')
    list_filter = ('grade', 'driver', 'supervisor')
    inlines = [FamilyContactInline]

@admin.register(FamilyContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'student', 'order')
    search_fields = ('name', 'student__name')

admin.site.site_header = 'إدارة النقل المدرسي'
admin.site.site_title = 'النقل المدرسي'
admin.site.index_title = 'لوحة التحكم'
