# Generated by Django 3.2.23 on 2023-11-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-dt',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Список заказов'},
        ),
        migrations.AlterModelOptions(
            name='parameter',
            options={'ordering': ('-name',), 'verbose_name': 'Название параметра', 'verbose_name_plural': 'Список названий параметров'},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
