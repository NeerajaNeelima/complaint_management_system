# Generated by Django 4.1.5 on 2023-01-26 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_app', '0005_complaints_registration_table_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Complaints_Registration_Table',
        ),
    ]
