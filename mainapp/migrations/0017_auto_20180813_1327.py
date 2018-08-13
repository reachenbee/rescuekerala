# Generated by Django 2.1 on 2018-08-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_contributor_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='districtneed',
            name='status',
        ),
        migrations.AddField(
            model_name='districtneed',
            name='cnandpts',
            field=models.TextField(default=' ', verbose_name='Contacts and collection points'),
            preserve_default=False,
        ),
    ]
