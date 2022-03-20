# Generated by Django 3.2.10 on 2022-03-19 12:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(help_text="Major types include 'block', 'unit', and 'sequence'.", max_length=50)),
                ('minor', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlockVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('identifier', models.CharField(max_length=255)),
                ('start_version_num', models.PositiveIntegerField()),
                ('end_version_num', models.PositiveIntegerField(default=2147483647)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LearningContext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('identifier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LearningContextVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('identifier', models.CharField(max_length=255)),
                ('version_num', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LearningContextBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('identifier', models.CharField(max_length=255)),
                ('block_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='learning_publishing.blocktype')),
                ('learning_context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_publishing.learningcontext')),
            ],
        ),
        migrations.AddConstraint(
            model_name='learningcontextblock',
            constraint=models.UniqueConstraint(fields=('learning_context_id', 'identifier'), name='learning_publishing_lcb_one_identifier_per_lc'),
        ),
    ]
