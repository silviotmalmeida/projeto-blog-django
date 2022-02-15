# Generated by Django 4.0.1 on 2022-02-15 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título')),
                ('data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
                ('excerto', models.TextField(verbose_name='Excerto')),
                ('imagem', models.ImageField(blank=True, upload_to='pictures/%Y/%m/', verbose_name='Imagem')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado')),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('id_categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categories.categoria', verbose_name='Categoria')),
            ],
        ),
    ]
