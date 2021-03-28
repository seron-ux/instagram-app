# Generated by Django 3.1.7 on 2021-03-28 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='comments',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('postt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.image')),
            ],
        ),
    ]