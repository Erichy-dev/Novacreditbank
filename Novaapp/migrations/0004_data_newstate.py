# Generated by Django 4.1 on 2022-09-12 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Novaapp', '0003_data_first_his_data_last_history_data_second_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='newstate',
            field=models.TextField(blank=True, null=True),
        ),
    ]