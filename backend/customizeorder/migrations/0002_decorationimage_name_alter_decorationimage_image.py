# Generated by Django 4.0.4 on 2022-08-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customizeorder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='decorationimage',
            name='name',
            field=models.CharField(default='No Image', max_length=30),
        ),
        migrations.AlterField(
            model_name='decorationimage',
            name='image',
            field=models.ImageField(upload_to='tool'),
        ),
    ]
