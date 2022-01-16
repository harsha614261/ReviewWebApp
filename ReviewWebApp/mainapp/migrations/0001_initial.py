# Generated by Django 3.2.11 on 2022-01-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Product_name', models.CharField(max_length=20)),
                ('Review', models.CharField(max_length=100)),
                ('Rating', models.IntegerField()),
                ('Recommendation', models.BooleanField(default=False)),
            ],
        ),
    ]