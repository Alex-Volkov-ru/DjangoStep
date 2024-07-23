# Generated by Django 5.0.6 on 2024-07-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='women',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='women',
            index=models.Index(fields=['-time_create'], name='women_women_time_cr_9f33c2_idx'),
        ),
    ]
