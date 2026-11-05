import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    """Give Publication.authors an explicit through model with a position.

    The auto-created join table berkeley_publication_authors already has the
    right columns, so we only tell Django's state about it (no table rebuild,
    existing links are kept), then add the position column for real.
    """

    dependencies = [
        ('berkeley', '0005_review_pub_types'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Authorship',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('publication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berkeley.publication')),
                        ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='berkeley.person')),
                    ],
                    options={
                        'db_table': 'berkeley_publication_authors',
                        'ordering': ['position', 'id'],
                        'unique_together': {('publication', 'person')},
                    },
                ),
                migrations.AlterField(
                    model_name='publication',
                    name='authors',
                    field=models.ManyToManyField(blank=True, related_name='authors', through='berkeley.Authorship', to='berkeley.person'),
                ),
            ],
        ),
        migrations.AddField(
            model_name='authorship',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
