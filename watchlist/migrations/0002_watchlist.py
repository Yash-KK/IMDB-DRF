# Generated by Django 4.2 on 2023-05-06 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
                ('total_reviews', models.IntegerField(default=0)),
                ('avg_ratings', models.FloatField(default=0)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='watchlist.streamingplatform')),
            ],
            options={
                'verbose_name': 'WatchList',
                'verbose_name_plural': "WatchList's",
            },
        ),
    ]
