# Generated by Django 4.0.5 on 2022-06-12 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deserialize', '0005_year_alter_detail_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='date',
            field=models.CharField(max_length=15),
        ),
    ]
