# Generated by Django 3.2.2 on 2021-06-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210618_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
