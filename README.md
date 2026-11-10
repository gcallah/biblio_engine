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
  so they never overwrite an editor's change, but `bin/load_data.sh`
  (all loaders) is only for building a database from scratch: it refuses
  to run on a database that has editor logins.
