# Generated by Django 2.0.2 on 2018-02-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('lastname', models.CharField(max_length=120, unique=True)),
                ('email', models.EmailField(max_length=120, unique=True)),
            ],
        ),
    ]
