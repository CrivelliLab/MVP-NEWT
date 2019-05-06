'''
queries.py
File contains template SQL commands for working with MIMIC-III sqlite database.
Strings have been made to be easily formatted according to some set of variable attributes.
For example, to use the get_table_vars command on noteevents do:

get_table_vars.format(table='noteevents')

'''

# GENERAL COMMANDS
get_tables = "SELECT name FROM sqlite_master WHERE type='table';"
get_table_vars = "SELECT sql FROM sqlite_master WHERE name='{table}';"

# NOTE EVENTS COMMANDS
get_notes_forpatient = "SELECT hadm_id, chartdate, category, text \
                        FROM noteevents WHERE subject_id='{pid}' \
                        ORDER BY chartdate DESC;"