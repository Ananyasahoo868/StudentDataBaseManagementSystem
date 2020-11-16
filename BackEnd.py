import sqlite3

def studentData() :
	con = sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,StdId text, FirstName text, SurName text, DoB text,Gender text,Age text, Address text,MobileNo text)")

	con.commit()
	con.close()


def addStdRec(StdId,FirstName,SurName,DoB,Gender,Address,MobileNo):
	con = sqlite3.connect("student.db")
	cur = con.cursor()
	cur.execute("INSERT INTO VALUES (NULL, ?,?,?,?,?,?,?,?)", StdId,FirstName,SurName,DoB,Age,Gender,Address,MobileNo)
	con.commit()
	con.close()

def viewData() :
	con = sqlite3.connect("student.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM student")
	row = cur.fetchall()
	con.close()
	return row

def deleteRec() :
	con = sqlite3.connect("student.db")
	cur = con.cursor()
	cur.execute("DELETE FROM student WHERE id=?",(id,))
	con.commit()
	con.close()

def searchData(StdId="",FirstName="",SurName="",DoB="",Age="",Gender="",Address="",MobileNo="") :
	con.sqlite3.connect("student.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM student where StdId=? OR FirstName=? OR SurName=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?",(StdId,FirstName,SurName,DoB,Age,Gender,Address,MobileNo))
	rows = cur.fetchall()
	con.close()
	return rows

def dataUpdate(id,StdId="",FirstName="",SurName="",DoB="",Age="",Gender="",Address="",MobileNo="") :
	con.sqlite3.connect("student.db")
	cur = con.cursor()
	cur.execute("UPDATE student SET StdId=?, FirstName=?, SurName=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=? WHERE id=?",(StdId,FirstName,SurName,DoB,Age,Gender,Address,MobileNo,id))
	con.commit()
	con.close()





	











studentData()