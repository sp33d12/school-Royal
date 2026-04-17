from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('transport', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='الصورة'),
        ),
        migrations.AddField(
            model_name='student',
            name='notes',
            field=models.TextField(blank=True, verbose_name='ملاحظات'),
        ),
    ]
