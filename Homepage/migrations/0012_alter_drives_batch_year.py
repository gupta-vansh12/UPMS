# Generated by Django 3.2.10 on 2023-05-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0011_alter_user_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drives',
            name='batch_year',
            field=models.IntegerField(default=2023, verbose_name='year'),
        ),
    ]