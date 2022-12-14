# Generated by Django 3.2.10 on 2022-08-29 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CandidateApp', '0002_auto_20220829_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetails',
            name='candidatedetails',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='CandidateApp.candidatedetails'),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='techskills',
            name='candidatedetails',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='CandidateApp.candidatedetails'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='techskills',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidatedetails',
            name='CandidateId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='CandidateId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='techskills',
            name='CandidateId',
            field=models.IntegerField(),
        ),
    ]
