# Generated by Django 3.2.3 on 2021-07-15 13:55

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210711_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='phone',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Amount to offer'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('OFFERED', 'Offer Made'), ('ACCEPTED', 'Offer Accepted'), ('DENIED', 'Offer Denied'), ('PROCESSING', 'Payment Processing'), ('COMPLETED', 'Payment Completed')], default='PENDING', max_length=32),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='county',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='full_name',
            field=models.CharField(default='kevin james', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='phone_number',
            field=models.CharField(default='09178478378', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='street_address1',
            field=models.CharField(default='11 Melon Street', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='town_or_city',
            field=models.CharField(default='Valle Verde 1', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='zipcode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]