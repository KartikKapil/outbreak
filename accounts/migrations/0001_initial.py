# Generated by Django 3.0.1 on 2020-01-18 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('user_type', models.CharField(choices=[('P', 'Patient'), ('H', 'Hospital')], default='Patient', max_length=2)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date-joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last-login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=3)),
                ('count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('age', models.IntegerField(default=None)),
                ('gender', models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('Others', 'O')], default='Male', max_length=6)),
                ('contact_no', models.IntegerField(unique=True)),
                ('social_status', models.CharField(choices=[('SC', 'SC'), ('General', 'Gen'), ('ST', 'ST'), ('OBC', 'OBC')], default='Gen', max_length=8)),
                ('prefd_hospital', models.CharField(max_length=100)),
                ('tokenNo', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('bed_capacity', models.CharField(max_length=250)),
                ('currently_free', models.CharField(max_length=250)),
                ('hasTokenSystem', models.BooleanField(default=False)),
                ('linkToTokenWebsite', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
