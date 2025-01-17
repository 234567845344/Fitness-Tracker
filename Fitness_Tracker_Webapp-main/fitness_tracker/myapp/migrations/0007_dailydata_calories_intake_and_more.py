# Generated by Django 4.2.2 on 2023-10-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_dailydata'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailydata',
            name='calories_intake',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='dailydata',
            name='calories_burned',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
