#!/usr/bin/python
import sqlite3

def extract_data_from_table(conn, table_name):
    c = conn.cursor()
    with open(f'{table_name}_data.sql', 'w') as f:
        for row in c.execute(f"SELECT * FROM {table_name}"):
            row_data = ', '.join(map(repr, row))
            f.write(f"INSERT INTO {table_name} VALUES ({row_data});\n")
    c.close()

conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

print("Starting extract job..")
for table_details in c.execute("SELECT name FROM sqlite_master WHERE type='table'"):
    table_name = table_details[0]
    print("Extracting data for table: " + table_name)
    extract_data_from_table(conn, table_name)

c.close()
