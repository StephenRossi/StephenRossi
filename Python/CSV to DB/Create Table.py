import sqlite3, sys, time

db = sqlite3.connect('CSVDataTransfer.db')

db.execute('''CREATE TABLE Data(
             Data TEXT PRIMARY KEY NOT NULL);''')

db.commit()
db.close()
        
