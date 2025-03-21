import sqlite3



conn = sqlite3.connect('temperature.db')

c = conn.cursor()
c.execute("")
c.execute("")
conn.commit()

c = conn.cursor()
c.execute("INSERT INTO temperature (`devicename`, `temp`, `timestamp`) VALUES('test', 29, datetime('now', 'localtime'))")
conn.commit()

c = conn.cursor()
c.execute("INSERT INTO temperature (`devicename`, `temp`, `timestamp`) VALUES('test', 35, datetime('now', 'localtime'))")
conn.commit()

conn.close()

# conn = sqlite3.connect('temperature.db')
# c = conn.cursor()
# c.execute('SELECT devicename, AVG(temp) AS averagetemp FROM temperature GROUP BY devicename ORDER BY devicename ASC')
# results = c.fetchall()

# for result in results:
			
	# print('devicename = {}; average temperature = {}'.format(result[0], result[1]))
