# Generated by Django 3.1.5 on 2021-02-13 20:41

import common.models
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Název')),
            ],
            options={
                'verbose_name': 'Stupeň školy',
                'verbose_name_plural': 'Stupně škol',
                'ordering': ('name',),
            },
            bases=(models.Model, common.models.GraphModel),
        ),
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Název')),
            ],
            options={
                'verbose_name': 'Typ školy',
                'verbose_name_plural': 'Typy škol',
                'ordering': ('name',),
            },
            bases=(models.Model, common.models.GraphModel),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='Název předmětu')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Zkratka')),
            ],
            options={
                'verbose_name': 'Vzdělávací oblast podle RVP',
                'verbose_name_plural': 'Vzdělávací oblasti podle RVP',
                'ordering': ('name',),
            },
            bases=(models.Model, common.models.GraphModel),
        ),
        migrations.CreateModel(
            name='SubjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Název')),
                ('subjects', models.ManyToManyField(to='teaching.Subject', verbose_name='Předměty')),
            ],
            options={
                'verbose_name': 'Předmětová skupina',
                'verbose_name_plural': 'Předmětové skupiny',
                'ordering': ('name',),
            },
            bases=(models.Model, common.models.GraphModel),
        ),
    ]
