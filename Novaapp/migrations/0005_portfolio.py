# Generated by Django 4.1 on 2022-09-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Novaapp', '0004_data_newstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ben_name', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=200)),
            ],
        ),
    ]