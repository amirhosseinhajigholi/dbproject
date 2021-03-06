# Generated by Django 2.2 on 2021-01-31 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PA_type', models.CharField(max_length=32)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('PA_id', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='PR_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
