# Generated by Django 2.2.5 on 2019-09-10 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_post_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True, serialize=False,
                    verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL, verbose_name='Автор', )),
                ('post', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='blog.Post', verbose_name='Пост, к которому написан', related_name='comments to post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(
                related_name='posts', to='blog.Tag',
                verbose_name='Теги поста'),
        ),
    ]
