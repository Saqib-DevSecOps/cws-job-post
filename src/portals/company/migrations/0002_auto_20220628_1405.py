# Generated by Django 3.2 on 2022-06-28 09:05

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact_address',
        ),
        migrations.AddField(
            model_name='candidate',
            name='about',
            field=models.TextField(blank=True, help_text='Say something about yourself, your love to hear you, briefly describe yourself, interests etc', null=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='degree',
            field=models.CharField(choices=[('ssc', 'Matric'), ('hssc', 'F.sc'), ('bs', 'Bachelors'), ('ms', 'Master'), ('phd', 'Doctorate')], default='ssc', help_text="Name of Field in which you have passed bachelors - Leave blank if you don't have bachelors degree", max_length=15),
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.PositiveIntegerField(default=0, help_text='Years of working experience'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='previous_company',
            field=models.CharField(blank=True, help_text='Leave blank if not', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='company_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='company_registration_no',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='company_start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date started'),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='job',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='company.job'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('acc', 'Accepted'), ('pen', 'Pending'), ('app', 'Applied')], default='app', max_length=3),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='business_type',
            field=models.CharField(choices=[('per', 'Personal'), ('pre', 'Premium'), ('ent', 'Enterprise')], default='per', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='tag_line',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_provider', to='company.company'),
        ),
        migrations.AlterField(
            model_name='job',
            name='detailed_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('o', 'Open'), ('c', 'Close')], default='o', max_length=1),
        ),
    ]