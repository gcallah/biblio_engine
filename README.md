# biblio_engine
Django project to create a customized bibliography engine for anyone who needs one.

The engine will allow easy imports and exports, and search on multiple fields, as well as drill-down data on publishers, authors, journals, etc.

## Editing and the live database

The live site (moabiblio.pythonanywhere.com) runs on its own SQLite
database, `~/mysite/db.sqlite3` on PythonAnywhere. That copy is the master:
trusted editors log in (the Login link on the menu) and edit records
through the Django admin, reached by the edit pencils on the site.
`db.sqlite3` is not in git, and every deploy backs the live copy up to
`~/db_backups` on the server (keeping the last 30) and runs migrations.

- **Logins**: there is no sign-up. On PythonAnywhere, in `~/mysite` with
  the `biblio` virtualenv, run `python manage.py add_editor <username>`;
  it asks for the password. Re-running it resets the password. Every
  editor can edit everything.
- **Bulk loads**: download the live copy with `bin/pull_live_db.sh`, run
  just the new loader on it, check the result, and upload it with
  `bin/push_live_db.sh`, which refuses if anyone has edited the site
  since the download. Both need the moabiblio password in
  `MOABIBLIO_PWD`. Loaders only fill blank fields of existing records,
  so they never overwrite an editor's change. But they find existing
  records by title, so re-running an old loader on the live data would
  load a record again if an editor has corrected its title: run only the
  new loader. `bin/load_data.sh` (all loaders) is for building a database
  from scratch, and refuses to run on a database that has editor logins.
- **Corrections** are made in the admin on the live site, not by editing
  the loaders' data files.
- **The editors' to-do list** is on the To do page (on the menu for
  editors): open questions about entries, and possible entries still to
  decide on. Both are kept in the live database and edited in the admin.
  `manage.py load_editors_todo` started the list of possible entries
  from `docs/works_mentioning_triage.csv`; since then the live database,
  not the CSV, is the up-to-date list. Editors add new entries with the
  Add entry link on the menu.
