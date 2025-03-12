# Generated by Django 4.2.19 on 2025-03-11 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oel_publishing', '0002_alter_learningpackage_key_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('publishable_entity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='oel_publishing.publishableentity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntityList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EntityListRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.PositiveIntegerField()),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='oel_publishing.publishableentity')),
                ('entity_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oel_publishing.entitylist')),
                ('entity_version', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='+', to='oel_publishing.publishableentityversion')),
            ],
        ),
        migrations.CreateModel(
            name='ContainerVersion',
            fields=[
                ('publishable_entity_version', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='oel_publishing.publishableentityversion')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='oel_publishing.container')),
                ('entity_list', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='container_versions', to='oel_publishing.entitylist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='entitylistrow',
            constraint=models.UniqueConstraint(fields=('entity_list', 'order_num'), name='oel_publishing_elist_row_order'),
        ),
    ]
