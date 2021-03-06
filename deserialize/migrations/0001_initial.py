# Generated by Django 4.0.5 on 2022-06-11 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PetroleumProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('sale', models.CharField(max_length=15)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deserialize.country')),
                ('petroleum_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deserialize.petroleumproduct')),
            ],
        ),
    ]
