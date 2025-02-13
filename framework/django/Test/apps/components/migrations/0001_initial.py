# Generated by Django 5.0.7 on 2024-08-03 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='姓名')),
                ('sex', models.BooleanField(default=True, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('classmate', models.CharField(db_column='class', max_length=5, verbose_name='班级编号')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='个性签名')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
                'db_table': 'components_student',
            },
        ),
    ]
