import sqlite3

conn = sqlite3.connect('test.db')
print ("opened database successfully")

conn.execute("DELETE FROM CRACK WHERE ID='3' AND NAME='Efraim Modechai' AND AGE='56")
conn.commit()
conn.close()
print ("Record Delted")
print ("Connection closed")
