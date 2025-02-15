# Generated by Django 2.2.6 on 2020-01-28 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Włączony')),
                ('sentry_sdk', models.CharField(blank=True, help_text='https://23ac1c5dc1ad4233a5176af52bdc3aaa@sentry.io/2035970', max_length=200, null=True, verbose_name='Sentry URL')),
            ],
            options={
                'verbose_name': 'Konfiguracja strony',
                'verbose_name_plural': 'Konfiguracje strony',
            },
        ),
    ]
