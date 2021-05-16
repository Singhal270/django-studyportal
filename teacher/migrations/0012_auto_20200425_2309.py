# Generated by Django 3.0.5 on 2020-04-25 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0011_auto_20200425_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.Section'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='email',
            field=models.CharField(default='name@mail', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='phone',
            field=models.CharField(default='1234', max_length=200, null=True),
        ),
    ]