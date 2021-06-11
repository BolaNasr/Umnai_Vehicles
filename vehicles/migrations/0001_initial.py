# Generated by Django 3.2.4 on 2021-06-10 19:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vin', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('make', models.CharField(max_length=60)),
                ('model', models.CharField(max_length=60)),
                ('seat_capacity', models.IntegerField()),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2021)])),
                ('type', models.CharField(choices=[('Car', 'Car'), ('Truck', 'Truck'), ('MotorCyclye', 'Motor Cyclye')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.vehicle')),
                ('roof_rack_availability', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
            ],
            bases=('vehicles.vehicle',),
        ),
        migrations.CreateModel(
            name='MotorCyclye',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.vehicle')),
                ('sidecar_availability', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
            ],
            bases=('vehicles.vehicle',),
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.vehicle')),
                ('haul_capacity', models.FloatField()),
            ],
            bases=('vehicles.vehicle',),
        ),
    ]
