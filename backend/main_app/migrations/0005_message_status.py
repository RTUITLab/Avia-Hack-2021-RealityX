# Generated by Django 3.2 on 2021-04-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_message_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='status',
            field=models.CharField(default='Обработано', max_length=256, verbose_name='Статус'),
        ),
    ]
