import django.db.models.deletion
from django.db import migrations, models


def number_editors(apps, schema_editor):
    """Give existing editors positions 1, 2, ... in the order they were
    added (the loaders add them in title-page order)."""
    Editorship = apps.get_model('berkeley', 'Editorship')
    last_pub, pos = None, 0
    for link in Editorship.objects.order_by('publication_id', 'id'):
        pos = pos + 1 if link.publication_id == last_pub else 1
        last_pub = link.publication_id
        link.position = pos
        link.save(update_fields=['position'])


class Migration(migrations.Migration):
    """Give Publication.editors an explicit through model with a position,
    as 0006 did for authors.

    The auto-created join table berkeley_publication_editors already has the
    right columns, so we only tell Django's state about it (no table rebuild,
    existing links are kept), add the position column, then number the
    existing links.
    """

    dependencies = [
        ('berkeley', '0006_authorship'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Editorship',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berkeley.publication')),
                        ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berkeley.person')),
                    ],
                    options={
                        'db_table': 'berkeley_publication_editors',
                        'ordering': ['position', 'id'],
                        'unique_together': {('publication', 'person')},
                    },
                ),
                migrations.AlterField(
                    model_name='publication',
                    name='editors',
                    field=models.ManyToManyField(blank=True, related_name='editors', through='berkeley.Editorship', to='berkeley.person'),
                ),
            ],
        ),
        migrations.AddField(
            model_name='editorship',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RunPython(number_editors, migrations.RunPython.noop),
    ]
