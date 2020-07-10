# Generated by Django 3.0.8 on 2020-07-10 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bomba',
            fields=[
                ('cod_bomba', models.IntegerField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=30)),
                ('n_estagio', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'bomba',
            },
        ),
        migrations.CreateModel(
            name='Curva',
            fields=[
                ('cod_curva', models.IntegerField(primary_key=True, serialize=False)),
                ('n_curva', models.CharField(max_length=10)),
                ('vazao_min', models.FloatField()),
                ('vazao_max', models.FloatField()),
            ],
            options={
                'db_table': 'curva',
            },
        ),
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('cod_motor', models.IntegerField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(max_length=30)),
                ('potencia', models.FloatField()),
                ('tensao', models.CharField(max_length=15)),
                ('n_fase', models.IntegerField()),
            ],
            options={
                'db_table': 'motor',
            },
        ),
        migrations.CreateModel(
            name='PontoCurva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vazao', models.FloatField()),
                ('altura', models.FloatField()),
                ('npsh', models.FloatField()),
                ('rend', models.FloatField()),
                ('cod_curva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphic.Curva')),
            ],
            options={
                'db_table': 'ponto_curva',
            },
        ),
        migrations.CreateModel(
            name='Acoplamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_bomba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphic.Bomba')),
                ('cod_curva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphic.Curva')),
                ('cod_motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graphic.Motor')),
            ],
            options={
                'db_table': 'acoplamento',
            },
        ),
    ]