# Generated by Django 4.0.6 on 2022-08-10 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_image', models.ImageField(upload_to='')),
                ('portfolio_heading', models.CharField(max_length=100)),
                ('portfolio_subheading', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Porfolio',
                'verbose_name_plural': 'My Porfolio',
            },
        ),
    ]