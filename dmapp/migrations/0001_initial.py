# Generated by Django 3.2 on 2021-05-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_id', models.IntegerField()),
                ('receiver_id', models.IntegerField()),
                ('content', models.CharField(max_length=500)),
                ('send_time', models.DateTimeField()),
            ],
        ),
    ]
