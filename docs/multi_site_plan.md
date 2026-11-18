# Plan: one engine, several bibliography sites

Goal: run a bibliography site per thinker (Oakeshott now, Voegelin next),
each at its own address and probably on its own server, sharing as much
code as possible.

Decision (2026-11-17): **one repository**, a shared engine plus one
package per site. Splitting the engine into a pip package of its own can
come later if there are many sites.

## Where the Oakeshott specifics live today

| Where | What |
|---|---|
| `berkeley/models.py` `TYPE_CHOICES` | "Books by Oakeshott" etc. The codes (BKBY, SWAB, ...) are already generic. |
| `/oakeshott/` URL prefix | Hardcoded about 40 times: `get_absolute_url`-style methods in `models.py`, every template, `settings.LOGIN_*`, `admin.site_url`, `add_editor.py`, `bin/check_pages.py`. |
| `base.html`, `about.html`, `static/berkeley/img/` | Header, footer, portrait, about text. |
| `admin.py` | Admin site header and title. |
| `management/commands/` | Nearly all of its ~21.8k lines are Oakeshott data. Only `_loaders.py` and `add_editor.py` are generic. |
| `deploy.sh`, `rebuild.sh`, `makefile` | `moabiblio` account, WSGI path and virtualenv hardcoded. |
| `migrations/0004`, `0005`, `0011` | Choice labels with "Oakeshott" serialized in. |

## Target layout

```
berkeley/              shared engine: models, views, forms, generic templates, _loaders.py
sites/oakeshott/       Django app: templates (about, header), static, data + load_* commands
sites/voegelin/        same structure
mysite/settings/base.py + oakeshott.py + voegelin.py
```

- Every server checks out the same repo and picks its site with
  `DJANGO_SETTINGS_MODULE`, with its own sqlite database.
- Each site package is a Django app, so its management commands and
  templates exist only on that site.
- The `berkeley` app label is **not** renamed: the table names
  (`berkeley_*`), the migration history and the live database depend on it.

## Phases

Pushing to master deploys the Oakeshott site, so every phase must leave
that site unchanged. Check the live site after each one.

0. **Safety net.** Pin Django (needs 5.0+ for callable choices) to the
   version already on the server. The tests and `bin/check_pages.py` are
   the regression net. *Done 2026-11-17: Django==6.1.3,
   django-extensions==4.1, matching PythonAnywhere.*
1. **No hardcoded `/oakeshott/`.** Use `reverse()` and
   Django's `url` template tag, and make the mount prefix a setting.
   Oakeshott keeps `/oakeshott/` (existing links); the `/berkeley/`
   redirect stays Oakeshott-only. *Done 2026-11-17: settings
   `BIBLIO_URL_PREFIX` and `BIBLIO_OLD_URL_PREFIXES`; `LOGIN_*` use URL
   names; empty publisher/journal links no longer rendered.*
2. **Site identity in settings.** A `BIBLIO_SITE` setting (short name,
   full name, portrait, admin titles) exposed through a context processor.
   Pub-type labels built from the short name ("Books by {short}"), with
   per-site overrides for different labels or enabled types. Migrations:
   labels are serialized into them, so use callable choices and confirm
   `makemigrations --check` is clean under every site's settings. Drop the
   leftover COVID `CATEGORIES` here. *Done 2026-11-17: `BIBLIO_SITE` (name, short
   name, dates, portrait, credits, `pub_type_labels`), the `biblio`
   context processor, `pub_type_choices()` with migration 0013 (no SQL);
   a test checks another site's settings need no migrations.*
3. **Templates and static files.** Site template and static dirs come
   before the engine's. `about.html` becomes wholly per-site; `base.html`
   gets its header, portrait and footer from settings. Move
   `oakeshott.jpg` and the Caius gate image into `sites/oakeshott/`.
   *Done 2026-11-18, except moving the images: `sites/oakeshott` is a
   Django app listed before `berkeley`, so its templates win; it has
   `about.html`, and the engine keeps a generic one. The background
   picture is `BIBLIO_SITE["background"]`, no longer in `style.css`.
   The images stay in `mysite/static/` for now, because on
   PythonAnywhere a static-files mapping serves `/static/` straight
   from that folder (Django never sees those requests). Moving them is
   part of phase 5.*
4. **Data out of the engine.** All `_*.py` data modules, the
   `load_*_oakeshott` commands, `book_info`, `_keywords`,
   `load_editors_todo`, their tests and `bin/load_data.sh` move to
   `sites/oakeshott/`. Engine tests run under a fake-subject test settings
   module, and CI runs the suite once per site.
5. **Deployment.** Parameterize `deploy.sh`, `rebuild.sh` and `makefile`
   (account, WSGI path, virtualenv, settings module). A second CI deploy
   job with Voegelin's secrets. Static files: set `STATIC_ROOT`, run
   `collectstatic` in `deploy.sh`, then repoint each server's `/static/`
   mapping (PythonAnywhere Web tab) at `STATIC_ROOT`; only after that,
   move the Oakeshott images into `sites/oakeshott/static/`. Note that
   `collectstatic` will also replace the very old admin files committed
   in `mysite/static/admin` (jQuery 2.1.4) with Django 6.1's, so check
   the admin add/change forms on the live site after that push.
6. **Voegelin.** Skeleton site package, empty migrated database, local
   smoke test, then deploy. Choose how its data comes in: loader modules
   like Oakeshott's, or a generic CSV/BibTeX import in the engine that
   later sites can reuse.

Later: links between sites (e.g. Voegelin works on Oakeshott, a
Collingwood site). Stable per-site URLs plus an "also in" field on
people and works would do it; not needed for the split.
