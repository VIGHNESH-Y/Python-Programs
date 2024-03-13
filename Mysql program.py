import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd='vighnesh123',database="student")
curs=db.cursor()
#curs.execute("drop table student")
curs.execute("CREATE TABLE student (roll_no INT,name VARCHAR(25),total INT(3),course VARCHAR(10),dob DATE)")
sql = "INSERT INTO student (roll_no, name,total,course,dob) VALUES (%s, %s,%s,%s,%s)"
val = [
("1",'Ritvik',"50",'CSC',"2004-12-25"),
("2","aa","23","CSC","2003-12-14"),
("3","BBB","234","CSC","2003-1-12"),
]
curs.executemany(sql, val)



db.commit()



print(curs.rowcount, "was inserted.")
