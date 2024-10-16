# Generated by Django 5.0.7 on 2024-07-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('detail', models.CharField(max_length=128, verbose_name='详细信息')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='余额'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=128, null=True, unique=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=16, verbose_name='姓名'),
        ),
    ]
