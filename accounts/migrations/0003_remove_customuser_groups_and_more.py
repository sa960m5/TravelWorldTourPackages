# Generated by Django 5.1.4 on 2025-03-03 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
