from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('berkeley', '0002_sync_state_with_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='institution',
        ),
    ]
