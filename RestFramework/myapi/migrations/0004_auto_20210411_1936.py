# Generated by Django 3.1.4 on 2021-04-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20210411_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]
