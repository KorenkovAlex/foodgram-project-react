# Generated by Django 3.2.16 on 2023-12-06 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('-author_id',), 'verbose_name': 'Подписка на пользователя', 'verbose_name_plural': 'Подписки на пользователей'},
        ),
    ]
