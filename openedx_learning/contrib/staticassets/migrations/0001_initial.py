# Generated by Django 3.2.10 on 2022-07-21 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itemstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ItemVersionAsset',
            fields=[
                ('item_version', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='itemstore.itemversion')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='staticassets.asset')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
