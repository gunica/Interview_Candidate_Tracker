# Generated by Django 3.2.10 on 2022-08-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateDetails',
            fields=[
                ('CandidateId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('CandidateId', models.AutoField(primary_key=True, serialize=False)),
                ('PhoneNumber', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=40)),
                ('Address', models.CharField(max_length=500)),
                ('Location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TechSkills',
            fields=[
                ('CandidateId', models.AutoField(primary_key=True, serialize=False)),
                ('Skills', models.CharField(max_length=50)),
            ],
        ),
    ]
