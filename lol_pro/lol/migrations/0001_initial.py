# Generated by Django 3.1.2 on 2020-12-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('cname', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cimg', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'champion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Itembuild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(blank=True, max_length=30, null=True)),
                ('item2', models.CharField(blank=True, max_length=30, null=True)),
                ('item3', models.CharField(blank=True, max_length=30, null=True)),
                ('pick', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('win', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'itembuild',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rimg1', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg2', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg3', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg4', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg5', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg6', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg7', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg8', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg9', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg10', models.CharField(blank=True, max_length=30, null=True)),
                ('rimg11', models.CharField(blank=True, max_length=30, null=True)),
                ('pick', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('win', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'lun',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pos',
            fields=[
                ('pname', models.CharField(blank=True, max_length=5, null=True)),
                ('pno', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'pos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(blank=True, max_length=30, null=True)),
                ('pick', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('win', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'shoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pimg', models.TextField(blank=True, null=True)),
                ('sk1img', models.TextField(blank=True, null=True)),
                ('s2img', models.TextField(blank=True, null=True)),
                ('s3img', models.TextField(blank=True, null=True)),
                ('s4img', models.TextField(blank=True, null=True)),
                ('s1', models.CharField(blank=True, max_length=2, null=True)),
                ('s2', models.CharField(blank=True, max_length=2, null=True)),
                ('s3', models.CharField(blank=True, max_length=2, null=True)),
                ('s4', models.CharField(blank=True, max_length=2, null=True)),
                ('s5', models.CharField(blank=True, max_length=2, null=True)),
                ('s6', models.CharField(blank=True, max_length=2, null=True)),
                ('s7', models.CharField(blank=True, max_length=2, null=True)),
                ('s8', models.CharField(blank=True, max_length=2, null=True)),
                ('s9', models.CharField(blank=True, max_length=2, null=True)),
                ('s10', models.CharField(blank=True, max_length=2, null=True)),
                ('s11', models.CharField(blank=True, max_length=2, null=True)),
                ('s12', models.CharField(blank=True, max_length=2, null=True)),
                ('s13', models.CharField(blank=True, max_length=2, null=True)),
                ('s14', models.CharField(blank=True, max_length=2, null=True)),
                ('s15', models.CharField(blank=True, max_length=2, null=True)),
                ('pick', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('win', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'skill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp1img', models.TextField(blank=True, null=True)),
                ('sp2img', models.TextField(blank=True, null=True)),
                ('pick', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('win', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'spell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Startitems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item1', models.CharField(blank=True, max_length=30, null=True)),
                ('item2', models.CharField(blank=True, max_length=30, null=True)),
                ('pick', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('win', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'startitems',
                'managed': False,
            },
        ),
    ]
