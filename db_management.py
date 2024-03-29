import re
import sqlite3


# Function to export SQLite database to SQL script
def export_sqlite_to_sql(sqlite_file, output_sql_file):
    with sqlite3.connect(sqlite_file) as connection:
        with open(output_sql_file, 'w') as output:
            for line in connection.iterdump():
                output.write('%s\n' % line)


# Function to generate INSERT INTO statements
def generate_insert_into_statements(input_sql_file, output_insert_sql_file):
    with open(input_sql_file, 'r') as file:
        sql_script = file.read()

    # Extract INSERT INTO statements using regular expressions
    insert_into_statements = re.findall(r'INSERT INTO ([^(]+) VALUES \(([^)]+)\);', sql_script)

    # Write INSERT INTO statements to output file
    with open(output_insert_sql_file, 'w') as output:
        for table, values in insert_into_statements:
            output.write(f'INSERT INTO {table} VALUES ({values});\n')


# Define input and output file paths
sqlite_file = 'db.sqlite3'
output_sql_file = 'exported_data.sql'
output_insert_sql_file = 'insert_data.sql'

# Export SQLite database to SQL script
export_sqlite_to_sql(sqlite_file, output_sql_file)

# Generate INSERT INTO statements
generate_insert_into_statements(output_sql_file, output_insert_sql_file)

print('Data migration completed.')
