# Generated by Django 3.2.9 on 2022-06-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lyb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('author', models.CharField(max_length=20, verbose_name='作者')),
                ('content', models.TextField()),
                ('is_delete', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'd_lyb',
            },
        ),
    ]
