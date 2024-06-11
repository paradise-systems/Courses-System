# Generated by Django 5.0.6 on 2024-06-11 00:45

import courses.models
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('level', models.CharField(choices=[('inicial', 'inicial'), ('intermedio', 'intermedio'), ('avanzado', 'avanzado')], default='inicial', max_length=20)),
                ('miniature', models.ImageField(default='miniatures/default.jpg', upload_to=courses.models.generar_nombre_miniatura)),
                ('num_leccions', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('miniature', models.ImageField(default='miniatures/default.jpg', upload_to=courses.models.generar_nombre_miniatura)),
                ('video', models.FileField(blank=True, null=True, upload_to=courses.models.generar_nombre_video)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leccions', to='courses.course')),
            ],
        ),
    ]
