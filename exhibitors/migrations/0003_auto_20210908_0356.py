# Generated by Django 3.1.2 on 2021-09-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0002_auto_20210907_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitor',
            name='logo',
            field=models.ImageField(upload_to='exhibitors'),
        ),
    ]