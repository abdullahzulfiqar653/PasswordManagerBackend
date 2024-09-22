# Generated by Django 4.2 on 2024-09-22 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models.mixins.uid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.CharField(editable=False, max_length=15, primary_key=True, serialize=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(null=True)),
                ('notes', models.TextField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('emoji', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passwords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('title', 'username', 'url', 'user')},
            },
            bases=(models.Model, main.models.mixins.uid.UIDMixin),
        ),
    ]