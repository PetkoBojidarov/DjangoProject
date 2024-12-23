# Generated by Django 5.1.2 on 2024-11-24 09:14

import CoockingWebsite.accounts.managers
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', CoockingWebsite.accounts.managers.CustomUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='cooking_level',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='customuser',
            name='cooking_level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
