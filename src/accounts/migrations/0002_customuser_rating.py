# Generated by Django 3.2.6 on 2021-09-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]