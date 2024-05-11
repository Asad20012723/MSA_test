# Generated by Django 5.0.1 on 2024-03-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_contact_delete_userinput'),
    ]

    operations = [
        migrations.CreateModel(
            name='RamadanDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='IqamahAdjustment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('prayer_name', models.CharField(max_length=50)),
                ('iqamah_time', models.TimeField()),
            ],
            options={
                'unique_together': {('date', 'prayer_name')},
            },
        ),
    ]
