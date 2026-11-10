"""Give someone a login, or reset an editor's password.

Editors can edit every record on the site (through the Django admin), so
they are made superusers. There is no sign-up page: logins are made with
this command, run where the live database is (PythonAnywhere):

    python manage.py add_editor <username> [--email you@example.com]

It asks for the password twice. Re-running it for an existing username
resets that editor's password.
"""
from getpass import getpass

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create an editor login (or reset an editor's password)."

    def add_arguments(self, parser):
        parser.add_argument("username")
        parser.add_argument("--email", default="")
        parser.add_argument("--password",
                            help="the password (otherwise you are asked "
                                 "for it, which keeps it out of your shell "
                                 "history)")

    def handle(self, *args, username, email, password, **options):
        if password is None:
            password = getpass("Password: ")
            if getpass("Password (again): ") != password:
                raise CommandError("The passwords don't match.")
        if not password:
            raise CommandError("The password can't be empty.")
        user, is_new = User.objects.get_or_create(username=username)
        if email:
            user.email = email
        user.is_staff = user.is_superuser = user.is_active = True
        user.set_password(password)
        user.save()
        verb = "Created" if is_new else "Updated"
        self.stdout.write(f"{verb} editor {username!r}; they can log in at "
                          "/oakeshott/login/.")
