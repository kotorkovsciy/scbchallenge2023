# Generated by Django 4.2.1 on 2023-05-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0003_resume_title_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='salary',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
