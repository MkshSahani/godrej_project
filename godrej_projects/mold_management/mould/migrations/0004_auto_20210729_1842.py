# Generated by Django 3.1.5 on 2021-07-29 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mould', '0003_auto_20210729_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalcleaningpresent',
            name='mould_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='mould_cleaning', serialize=False, to='mould.mould'),
        ),
    ]