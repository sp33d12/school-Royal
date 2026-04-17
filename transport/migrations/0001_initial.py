from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='اسم السائق')),
                ('phone', models.CharField(max_length=30, verbose_name='رقم الهاتف')),
                ('line_number', models.CharField(blank=True, max_length=20, verbose_name='رقم الخط')),
            ],
            options={'verbose_name': 'سائق', 'verbose_name_plural': 'السائقون', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='LineSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='اسم المسؤولة')),
                ('phone', models.CharField(max_length=30, verbose_name='رقم الهاتف')),
                ('line_number', models.CharField(blank=True, max_length=20, verbose_name='رقم الخط')),
            ],
            options={'verbose_name': 'مسؤولة خط', 'verbose_name_plural': 'مسؤولات الخطوط', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='اسم التلميذ')),
                ('grade', models.CharField(max_length=50, verbose_name='المرحلة')),
                ('area', models.CharField(blank=True, max_length=150, verbose_name='منطقة السكن')),
                ('phone1', models.CharField(blank=True, max_length=30, verbose_name='هاتف 1')),
                ('phone2', models.CharField(blank=True, max_length=30, verbose_name='هاتف 2')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='students', to='transport.driver', verbose_name='السائق')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                    related_name='students', to='transport.linesupervisor', verbose_name='مسؤولة الخط')),
            ],
            options={'verbose_name': 'تلميذ', 'verbose_name_plural': 'التلاميذ', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='FamilyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='الاسم')),
                ('phone', models.CharField(blank=True, max_length=30, verbose_name='الهاتف')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='الترتيب')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                    related_name='contacts', to='transport.student')),
            ],
            options={'verbose_name': 'مخوّل', 'verbose_name_plural': 'المخوّلون', 'ordering': ['order']},
        ),
    ]
