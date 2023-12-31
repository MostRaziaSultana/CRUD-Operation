# Generated by Django 4.2.4 on 2023-08-09 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(upload_to='prof_pic/')),
                ('number', models.TextField(max_length=15)),
                ('age', models.FloatField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default=None, max_length=8)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu')], default=None, max_length=10)),
            ],
        ),
    ]
