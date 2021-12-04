# Generated by Django 3.2.9 on 2021-12-04 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iLearn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=150)),
                ('translation', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'numbers',
            },
        ),
    ]