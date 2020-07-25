# Generated by Django 3.0.7 on 2020-07-10 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200701_0437'),
        ('log', '0010_auto_20200710_0608'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('history', '0002_auto_20200610_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='logger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='log.Logger'),
        ),
        migrations.AlterField(
            model_name='history',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Project'),
        ),
        migrations.AlterField(
            model_name='history',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Team'),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]