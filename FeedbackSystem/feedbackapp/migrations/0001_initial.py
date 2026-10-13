from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=30)),
                ('teacher', models.CharField(blank=True, max_length=150)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('target', models.CharField(blank=True, max_length=150)),
                ('class_name', models.CharField(blank=True, max_length=100)),
                ('year', models.CharField(blank=True, max_length=50)),
                ('teaching', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('communication', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('support', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('growth', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'data',
            },
        ),
    ]
