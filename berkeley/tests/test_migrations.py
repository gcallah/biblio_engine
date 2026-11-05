"""Guard against models and migrations drifting apart again."""
from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class MigrationsTest(TestCase):
    def test_no_missing_migrations(self):
        out = StringIO()
        try:
            call_command("makemigrations", "--check", "--dry-run",
                         stdout=out, stderr=StringIO())
        except SystemExit:
            self.fail("Models have changes with no migration. Run "
                      "`python manage.py makemigrations`.\n" + out.getvalue())
