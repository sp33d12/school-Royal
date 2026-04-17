from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('transport', '0002_student_photo_notes'),
    ]
    operations = [
        migrations.AddField(
            model_name='student',
            name='landmark',
            field=models.CharField(blank=True, max_length=200, verbose_name='نقطة دالة'),
        ),
    ]
