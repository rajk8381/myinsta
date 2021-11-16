# Generated by Django 3.2.9 on 2021-11-16 04:07

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='p.png', upload_to='uploads/posts')),
                ('desc', models.TextField(max_length=1000)),
                ('post_type', models.CharField(choices=[('1', 'Public'), ('2', 'Private')], default='1', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive'), ('3', 'Blocked'), ('4', 'Spam')], default='1', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
