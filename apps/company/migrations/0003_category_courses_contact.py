# Generated by Django 4.0.6 on 2022-08-15 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('own_phone', models.IntegerField(default=998)),
                ('extra_phone', models.IntegerField(default=998)),
                ('message', models.CharField(max_length=120)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_contact', to='company.category_courses')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Apply',
            },
        ),
    ]
