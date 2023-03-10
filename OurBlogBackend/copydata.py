from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    help = 'Copy data from SQLite to PostgreSQL'

    def handle(self, *args, **options):
        with connections['default'].cursor() as sqlite_cursor, connections['ourblogdb'].cursor() as postgresql_cursor:
            # replace `your_postgresql_db_alias` with the alias of the PostgreSQL database in your `settings.py` file
            # get the list of tables in the SQLite database
            sqlite_cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in sqlite_cursor.fetchall()]

            # copy data from SQLite to PostgreSQL table by table
            for table_name in tables:
                # delete existing data in the PostgreSQL table
                postgresql_cursor.execute(f"DELETE FROM {table_name};")
                sqlite_cursor.execute(f"SELECT * FROM {table_name};")
                rows = sqlite_cursor.fetchall()
                for row in rows:
                    placeholders = ','.join(['%s'] * len(row))
                    postgresql_cursor.execute(
                        f"INSERT INTO {table_name} VALUES ({placeholders})", row)
