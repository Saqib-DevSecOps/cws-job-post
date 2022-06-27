# Generated by Django 4.0.5 on 2022-06-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20220310_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='bachelor_degree',
        ),
        migrations.AddField(
            model_name='candidate',
            name='degree',
            field=models.CharField(choices=[('ssc', 'Matric'), ('hssc', 'F.sc'), ('bs', 'Bachelors'), ('ms', 'Master'), ('phd', 'Doctorate')], default='ssc', help_text="Name of Field in which you have passed bachelors - Leave blank if you don't have bachelors degree", max_length=15),
        ),
    ]