# Generated by Django 4.1.4 on 2022-12-22 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_teacher_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]