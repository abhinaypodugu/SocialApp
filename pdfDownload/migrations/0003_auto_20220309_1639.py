# Generated by Django 2.2.7 on 2022-03-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfDownload', '0002_auto_20220309_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to='myimages/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imgText',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
