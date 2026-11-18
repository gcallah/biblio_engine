"""Guard against models and migrations drifting apart again."""
from io import StringIO

from django.core.management import call_command
from django.test import TestCase, override_settings


class MigrationsTest(TestCase):
    def test_no_missing_migrations(self):
        out = StringIO()
        try:
            call_command("makemigrations", "--check", "--dry-run",
                         stdout=out, stderr=StringIO())
        except SystemExit:
            self.fail("Models have changes with no migration. Run "
                      "`python manage.py makemigrations`.\n" + out.getvalue())

    def test_another_site_needs_no_migrations(self):
        """Type labels come from settings, so a site with another subject
        (or its own labels) must not need migrations of its own."""
        other = {"name": "Eric Voegelin", "short_name": "Voegelin",
                 "pub_type_labels": {"MENT": "Works Discussing Voegelin"}}
        with override_settings(BIBLIO_SITE=other):
            self.test_no_missing_migrations()
