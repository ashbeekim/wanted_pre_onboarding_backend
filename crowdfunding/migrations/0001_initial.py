# Generated by Django 4.0.4 on 2022-04-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participantCount', models.PositiveIntegerField(default=0, verbose_name='참여자 수')),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
    ]