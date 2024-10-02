import argparse
import os
import sqlite3
import pandas as pd

def load_csv_to_sqlite(csv_path, db_path, table_name):
    """Load CSV into an SQLite database."""
    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_path)

    # Load CSV into pandas DataFrame
    df = pd.read_csv(csv_path)

    # Create a table from the CSV in the SQLite database
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()
    print(f"Data from {csv_path} has been loaded into table '{table_name}' in {db_path}.")

def process_files(input_path, db_path):
    """Process files: If a folder, loop through all CSVs; if a file, process a single CSV."""
    if os.path.isdir(input_path):
        # Loop through all CSV files in the input folder
        for file_name in os.listdir(input_path):
            if file_name.endswith(".csv"):
                csv_file_path = os.path.join(input_path, file_name)
                table_name = os.path.splitext(file_name)[0]  # Use file name (without extension) as the table name
                load_csv_to_sqlite(csv_file_path, db_path, table_name)
    elif os.path.isfile(input_path) and input_path.endswith(".csv"):
        # Single CSV file case
        table_name = os.path.splitext(os.path.basename(input_path))[0]  # Use file name as table name
        load_csv_to_sqlite(input_path, db_path, table_name)
    else:
        print(f"Invalid input: {input_path} is neither a folder nor a CSV file.")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Load CSV(s) into SQLite database.')
    parser.add_argument('-i', '--input', type=str, required=True, help='Path to the input CSV file or folder containing CSV files')
    parser.add_argument('-d', '--database', type=str, default='example.db', help='Path to the SQLite database file')
    
    args = parser.parse_args()

    # Process input path (folder or single CSV file)
    process_files(args.input, args.database)
