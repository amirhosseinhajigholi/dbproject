# Generated by Django 2.2 on 2021-01-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210131_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PR_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
