# Generated by Django 4.1.5 on 2023-01-26 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_app', '0002_complaint_registration_table_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Complaint_Registration_Table',
        ),
        migrations.DeleteModel(
            name='Complaint_Registration_Table_Student',
        ),
    ]