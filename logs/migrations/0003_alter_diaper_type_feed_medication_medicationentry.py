# Generated by Django 5.0.1 on 2024-01-24 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_alter_diaper_notes_sleep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaper',
            name='type',
            field=models.CharField(choices=[('WT', 'Wet'), ('DY', 'Dirty'), ('WD', 'Wet and Dirty')], default='WT'),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='Feed start time')),
                ('end_time', models.DateTimeField(verbose_name='Feed end time')),
                ('type', models.CharField(choices=[('Breast', [('LB', 'Left Breast'), ('RB', 'Right Breast')]), ('FO', 'Formula'), ('SF', 'Solid Food')], default='LB')),
                ('notes', models.TextField(blank=True)),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.baby')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=50, verbose_name='medication')),
                ('default_dose', models.PositiveIntegerField(blank=True)),
                ('dose_unit', models.CharField(blank=True, choices=[('g', 'grams'), ('ml', 'millitres'), ('oz', 'ounces'), ('fl oz', 'fluid ounces'), ('dp', 'drops')], default='ml')),
                ('notes', models.TextField(blank=True)),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.baby')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
                ('baby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.baby')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logs.medication')),
            ],
        ),
    ]