# Generated by Django 5.0.1 on 2024-01-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeExplainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_input', models.TextField()),
                ('_output', models.TextField()),
            ],
            options={
                'db_table': 't_code_explainer',
            },
        ),
    ]