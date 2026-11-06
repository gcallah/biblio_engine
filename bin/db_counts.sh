#!/bin/bash
# Summarize the local db.sqlite3: publications by type and subject,
# and checks for duplicate people, publishers and journals.
# Usage: bin/db_counts.sh
cd "$(dirname "$0")/.."
sqlite3 -header -column db.sqlite3 <<'SQL'
SELECT pub_type, COUNT(*) AS n FROM berkeley_publication GROUP BY pub_type;
SELECT p.pub_type, s.name AS subject, COUNT(*) AS n
  FROM berkeley_publication p JOIN berkeley_subject s ON s.id = p.subject_id
  GROUP BY p.pub_type, s.name;
SELECT (SELECT COUNT(*) FROM berkeley_person) AS people,
       (SELECT COUNT(*) FROM berkeley_publisher) AS publishers,
       (SELECT COUNT(*) FROM berkeley_journal) AS journals;
SELECT 'duplicate person' AS problem, fname, lname, COUNT(*) AS n
  FROM berkeley_person GROUP BY fname, lname HAVING n > 1;
SELECT 'duplicate journal' AS problem, name, COUNT(*) AS n
  FROM berkeley_journal GROUP BY name HAVING n > 1;
SQL
