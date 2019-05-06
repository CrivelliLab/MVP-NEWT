'''
notes_app.py
Script to serve as a backend function to gather notes for patients in the 
MIMIC-III database.

'''
import argparse
from mimic_iii_sqlite.sqlite_api import *
from mimic_iii_sqlite.queries import get_notes_forpatient

if __name__ == '__main__':
    
    # Parse Arguments
    parser = argparse.ArgumentParser(description='Generate JSON of Patient Notes From MIMIC-III.')
    parser.add_argument('patient_id', type=str, help='ID of patient.')
    parser.add_argument('path', type=str, help='Path of JSON file.')
    args = parser.parse_args()
    
    # Query Database
    rows = query_database(get_notes_forpatient.format(pid=args.patient_id))
    
    # Save JSON
    path_to_json = args.path.split("/") + [args.patient_id+'.json']
    rows_to_json(rows, "hadm_id chartdate category text".split(), '/'.join(path_to_json))