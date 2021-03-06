# Generated by Django 2.2 on 2019-04-22 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190421_1236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('language', models.CharField(blank=True, choices=[('PY', 'Python'), ('CPP', 'C++'), ('C', 'C'), ('JS', 'JavaScript'), ('TS', 'TypeScript'), ('HTML', 'HTML'), ('CSS', 'CSS')], default='PY', max_length=4)),
                ('general', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.AlterField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(related_name='skills', to='projects.Skill'),
        ),
    ]
