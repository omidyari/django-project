# Generated by Django 4.0 on 2022-01-23 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Napp', '0002_post_counted_views_post_creted_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('massage', models.TextField()),
                ('creted_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='post',
        ),
    ]