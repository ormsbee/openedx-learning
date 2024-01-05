# Generated by Django 3.2.23 on 2024-01-05 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oel_publishing', '0002_alter_fk_on_delete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishableentity',
            name='learning_package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publishable_entities', to='oel_publishing.learningpackage'),
        ),
        migrations.AlterField(
            model_name='publishlogrecord',
            name='publish_log',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='oel_publishing.publishlog'),
        ),
    ]
