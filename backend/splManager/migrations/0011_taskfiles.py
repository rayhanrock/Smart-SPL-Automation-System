# Generated by Django 3.2.13 on 2023-02-03 11:44

from django.db import migrations, models
import django.db.models.deletion
import splManager.models


class Migration(migrations.Migration):

    dependencies = [
        ('splManager', '0010_alter_task_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(null=True, upload_to=splManager.models.content_file_name)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='splManager.task')),
            ],
        ),
    ]
