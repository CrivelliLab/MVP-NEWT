'''
sqlite_api.py
File contains functions to help query and format results on the 
MIMIC-III SQLLite database.

'''
import sqlite3
import json

sqlite_file = "/project/projectdirs/m1532/Projects_MVP/_datasets/mimiciii_sqlite/mimic3.db"

# Make JSON From Rows
def rows_to_json(rows, c_labels, path):
    json_data = {}
    for i,r in enumerate(rows):
        json_data[i] = {}
        for j,c in enumerate(c_labels):
            json_data[i][c] = str(r[j])
    with open(path, 'w') as f: json.dump(json_data, f)
        
# Query Database
def query_database(sql_query):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute(sql_query)
    rows = c.fetchall()
    c.close()
    return rows