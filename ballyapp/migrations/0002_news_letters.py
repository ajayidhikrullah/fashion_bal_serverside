# Generated by Django 2.0.7 on 2018-11-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='news_letters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
