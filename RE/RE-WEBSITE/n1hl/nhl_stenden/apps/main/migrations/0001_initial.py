# Generated by Django 4.0.4 on 2022-07-24 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('rates', models.IntegerField()),
                ('text', models.TextField()),
                ('date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('zone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('birth_date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('zone_id', models.AutoField(primary_key=True, serialize=False)),
                ('zone_data', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('time_slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
