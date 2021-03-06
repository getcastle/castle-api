# Generated by Django 2.0.3 on 2018-04-09 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20180409_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicenetworkattributes',
            name='id',
        ),
        migrations.AlterField(
            model_name='device',
            name='attributesId',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='devicenetworkattributes',
            name='device',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='networking', serialize=False, to='devices.Device'),
        ),
    ]
