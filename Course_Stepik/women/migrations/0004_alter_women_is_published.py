# Generated by Django 5.0.6 on 2024-07-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_alter_women_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=1),
        ),
    ]
