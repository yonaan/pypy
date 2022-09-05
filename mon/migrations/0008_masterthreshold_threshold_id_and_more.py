# Generated by Django 4.0.5 on 2022-08-05 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon', '0007_remove_masterthreshold_sensor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='masterthreshold',
            name='threshold_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='temperature_data',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
