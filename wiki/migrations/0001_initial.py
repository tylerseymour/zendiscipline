# Generated by Django 3.1.4 on 2021-01-05 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'nodes',
            },
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'relationship_types',
            },
        ),
        migrations.CreateModel(
            name='NodeRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related', to='wiki.node')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='wiki.node')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wiki.relationshiptype')),
            ],
            options={
                'db_table': 'nodes_relations',
            },
        ),
        migrations.AddField(
            model_name='node',
            name='nodes',
            field=models.ManyToManyField(related_name='_node_nodes_+', through='wiki.NodeRelation', to='wiki.Node'),
        ),
        migrations.AddField(
            model_name='node',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]