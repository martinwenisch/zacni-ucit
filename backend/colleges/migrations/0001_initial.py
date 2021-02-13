# Generated by Django 3.1.5 on 2021-02-13 20:41

import common.models
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teaching', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Název školy')),
                ('type', models.CharField(choices=[('univerzitni', 'univerzitní'), ('neuniverzitni', 'neuniverzitní')], max_length=20, verbose_name='Typ')),
                ('form', models.CharField(choices=[('soukroma', 'soukromá'), ('statni', 'státní'), ('verejna', 'veřejná')], max_length=20, verbose_name='Forma')),
                ('address', models.CharField(max_length=200, verbose_name='Adresa')),
                ('rid', models.CharField(max_length=20, unique=True, verbose_name='RID')),
                ('ic', models.CharField(max_length=20, verbose_name='IČ')),
                ('databox', models.CharField(max_length=20, verbose_name='Datová schránka')),
                ('url', models.URLField(verbose_name='URL')),
                ('code', models.CharField(max_length=30, unique=True, verbose_name='Zkratka')),
            ],
            options={
                'verbose_name': 'Vysoká škola',
                'verbose_name_plural': 'Vysoké školy',
                'ordering': ('name',),
            },
            bases=(models.Model, common.models.GraphModel),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=200, verbose_name='Název fakulty')),
                ('rid', models.CharField(max_length=20, verbose_name='RID')),
                ('url', models.URLField(verbose_name='URL')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colleges.college')),
            ],
            options={
                'verbose_name': 'Fakulta vysoké školy',
                'verbose_name_plural': 'Fakulty vysokých škol',
                'ordering': ('name', 'college'),
                'unique_together': {('name', 'college')},
            },
            bases=(models.Model, common.models.GraphModel),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=300, verbose_name='Název')),
                ('price', models.IntegerField(verbose_name='Cena')),
                ('sds', models.IntegerField(verbose_name='Standardní doba studia')),
                ('form_present', models.BooleanField(default=False, verbose_name='Prezenční forma studia')),
                ('form_combined', models.BooleanField(default=True, verbose_name='Kombinovaná forma studia')),
                ('url', models.URLField(verbose_name='URL na podrobnější informace')),
                ('note', models.TextField(blank=True, verbose_name='Poznámka')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='colleges.faculty', verbose_name='Fakulta')),
                ('subjects', models.ManyToManyField(to='teaching.Subject', verbose_name='Předměty')),
            ],
            options={
                'verbose_name': 'Kurz',
                'verbose_name_plural': 'Kurzy',
                'ordering': ('name', 'faculty', 'faculty__college'),
            },
        ),
    ]
