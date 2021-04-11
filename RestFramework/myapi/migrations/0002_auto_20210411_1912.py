# Generated by Django 3.1.4 on 2021-04-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={},
        ),
        migrations.RenameField(
            model_name='university',
            old_name='name',
            new_name='clgname',
        ),
        migrations.RemoveField(
            model_name='student',
            name='university',
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='university',
            name='place',
            field=models.CharField(default='', max_length=50),
        ),
    ]