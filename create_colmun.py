import sqlite3
import sys
conn = sqlite3.connect('db/'+sys.argv[1]+'.db')
print ("Opened database successfully");
qurey = 'CREATE TABLE ' + sys.argv[2] +' ('
for i in range(3,len(sys.argv[3:]),2):
	if i != 3:
		qurey +=', '
	qurey+= sys.argv[i] +' ' +sys.argv[i+1]
qurey += ')'
print(qurey)
conn.execute(qurey)
print ("Table created successfully");
conn.close()

