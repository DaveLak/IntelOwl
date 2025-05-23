# Generated by Django 4.2.17 on 2025-01-15 09:34

from django.db import migrations


def migrate(apps, schema_editor):
    EngineConfig = apps.get_model("engines_manager", "EngineConfig")
    if not EngineConfig.objects.exists():
        EngineConfig.objects.create(
            modules=["malware_family.MalwareFamilyEngineModule"]
        )


class Migration(migrations.Migration):

    dependencies = [
        ("engines_manager", "0002_alter_engineconfig_modules"),
    ]

    operations = [
        migrations.RunPython(migrate, migrations.RunPython.noop),
    ]
