# Generated by Django 5.1 on 2024-08-18 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Draft', 'Published')], default='Draft', max_length=20),
        ),
    ]
