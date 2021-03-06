# Generated by Django 2.2 on 2019-04-21 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PorjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('techUsed', models.TextField()),
                ('description', models.TextField()),
                ('github', models.URLField()),
                ('url', models.URLField()),
                ('dateAdded', models.DateField(auto_now_add=True)),
                ('lastModified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
