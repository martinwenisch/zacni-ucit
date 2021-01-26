# Generated by Django 3.1.5 on 2021-01-23 15:50

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Zkratka')),
            ],
            options={
                'verbose_name': 'Vysoká škola',
                'verbose_name_plural': 'Vysoké školy',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=200, verbose_name='Název fakulty')),
                ('town', models.CharField(max_length=50, verbose_name='Město')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colleges.college')),
            ],
            options={
                'verbose_name': 'Fakulta vysoké školy',
                'verbose_name_plural': 'Fakulty vysokých škol',
                'ordering': ('name', 'college'),
                'unique_together': {('name', 'college', 'town')},
            },
        ),
    ]