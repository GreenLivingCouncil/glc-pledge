To get started:

1. Clone repo into your Stanford cgi-bin directory (requires WebAuth to work)
2. Create a SQLite database with the given script:
    sqlite3 bin/pledges.db < bin/sql/setup.sql
3. Copy js/config.sample.js to js/config.js to try out a sample configuration.
4. Update the root and cgi-bin paths in js/config.js to point to your own directories.

