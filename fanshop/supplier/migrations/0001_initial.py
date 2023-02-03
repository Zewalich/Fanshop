# Generated by Django 4.1.4 on 2023-01-23 10:11

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('company', models.CharField(max_length=255)),
                ('fortune', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'verbose_name': 'Основатель',
                'verbose_name_plural': 'Основатели',
                'ordering': ['second_name'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', django_countries.fields.CountryField(default='Germany', max_length=2)),
                ('contact', models.EmailField(max_length=254)),
                ('attribute', models.CharField(max_length=255)),
                ('info', models.TextField(blank=True)),
                ('founding_date', models.DateField(blank=True, null=True)),
                ('found', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.founder')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['name'],
            },
        ),
    ]