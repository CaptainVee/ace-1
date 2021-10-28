# Generated by Django 3.2.6 on 2021-10-28 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0010_alter_announcement_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='message',
            field=django_quill.fields.QuillField(default='ssss'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='announcement',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 20, 6, 37, 794942, tzinfo=utc)),
        ),
    ]
