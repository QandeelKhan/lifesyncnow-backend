import sqlite3
import psycopg2

# Connect to the SQLite database
sqlite_conn = sqlite3.connect('db.sqlite3')
sqlite_cursor = sqlite_conn.cursor()

# Connect to the PostgreSQL database
pg_conn = psycopg2.connect(
    host='localhost',
    database='ourblogdb',
    user='ourbloguser',
    password='OurBlogPassword'
)
pg_cursor = pg_conn.cursor()

# Get the list of tables in the SQLite database
tables_query = "SELECT name FROM sqlite_master WHERE type='table'"
sqlite_cursor.execute(tables_query)
tables = sqlite_cursor.fetchall()

# Loop through each table and copy the data to PostgreSQL
for table in tables:
    table_name = table[0]

    # Get the list of columns in the SQLite table
    columns_query = f"PRAGMA table_info({table_name})"
    sqlite_cursor.execute(columns_query)
    columns = sqlite_cursor.fetchall()

    # Build the CREATE TABLE query for PostgreSQL
    create_table_query = f"CREATE TABLE {table_name} ("

    for column in columns:
        column_name = column[1]
        column_type = column[2]

        if column_type == 'integer':
            pg_type = 'INTEGER'
        elif column_type == 'varchar(255)':
            pg_type = 'VARCHAR(255)'
        elif column_type == 'text':
            pg_type = 'TEXT'
        elif column_type == 'timestamp':
            pg_type = 'TIMESTAMP'
        else:
            raise Exception(f"Unhandled column type: {column_type}")

        create_table_query += f"{column_name} {pg_type}, "

    # Remove trailing comma and space
    create_table_query = create_table_query[:-2]
    create_table_query += ")"

    # Create the table in PostgreSQL
    pg_cursor.execute(create_table_query)
    pg_conn.commit()

    # Copy the data from SQLite to PostgreSQL
    copy_data_query = f"COPY {table_name} FROM STDIN WITH CSV HEADER DELIMITER ','"
    pg_cursor.copy_expert(copy_data_query, sqlite_cursor)
    pg_conn.commit()

print("Data migration complete.")
