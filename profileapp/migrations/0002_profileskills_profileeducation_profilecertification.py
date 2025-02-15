# Generated by Django 4.2.13 on 2024-07-02 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profileskills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('percentage', models.FloatField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('instituteyear', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileapp.profile')),
            ],
        ),
    ]
