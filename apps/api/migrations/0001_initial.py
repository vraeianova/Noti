# Generated by Django 3.2 on 2022-12-16 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(db_column='IdNote', primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, db_column='Note', max_length=255, null=True)),
                ('is_completed', models.BooleanField(db_column='IsCompleted', default=True)),
            ],
        ),
    ]
