# Generated by Django 4.1.4 on 2023-01-24 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Makeproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('sell_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('price_makeproduct', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('price_pro_fromshop', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('profit', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('loss', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('org_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.makeproduct')),
            ],
        ),
    ]
