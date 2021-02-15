# Generated by Django 3.1.5 on 2021-02-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0003_schoollevel_subjects'),
        ('qualifications', '0002_auto_20210206_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationtype',
            name='school_levels',
            field=models.ManyToManyField(related_name='education_types', to='teaching.SchoolLevel'),
        ),
    ]