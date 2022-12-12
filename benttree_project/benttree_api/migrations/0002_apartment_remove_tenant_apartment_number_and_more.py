# Generated by Django 4.1.3 on 2022-12-12 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benttree_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=7)),
                ('property', models.CharField(max_length=25)),
                ('occupants', models.IntegerField()),
                ('date_available', models.DateField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='apartment_number',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='lease_end',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='lease_start',
        ),
        migrations.AddField(
            model_name='tenant',
            name='email',
            field=models.EmailField(default='@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='apartment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='benttree_api.apartment'),
        ),
    ]