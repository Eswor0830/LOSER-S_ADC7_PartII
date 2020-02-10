# Generated by Django 3.0.3 on 2020-02-10 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('company_location', models.CharField(max_length=20)),
                ('package_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FreeLancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('Mobile_No', models.IntegerField()),
                ('Location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cash', models.IntegerField()),
                ('Cheque', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tourist_Name', models.CharField(max_length=20)),
                ('Tourist_Email', models.EmailField(max_length=30)),
                ('Tourist_Mobile_No', models.IntegerField()),
                ('Tourist_address', models.CharField(max_length=30)),
                ('Guide', models.ManyToManyField(blank=True, related_name='guide', to='face_of_nepal_Relationship.FreeLancer')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Guide', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_guide', to='face_of_nepal_Relationship.FreeLancer')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='face_of_nepal_Relationship.FreeLancer')),
            ],
        ),
    ]
