# Generated by Django 3.0.5 on 2020-04-28 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200425_2309'),
        ('teacher', '0012_auto_20200425_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='friends',
            field=models.ManyToManyField(blank=True, to='student.Stud'),
        ),
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Section'),
        ),
    ]
