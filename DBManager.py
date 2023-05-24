import sqlite3 as sql
from imageProcessing import imageProc, imageProcc
import numpy as np
import io
#]}

#name =  input('Enter your full name\t')
#data = imageProc()
dist = 7.3
#print(dist,dist.shape)
#pin = 5348#input("Enter pin\t")
#id = 1

def adaptArray(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sql.Binary(out.read())

def convertArray(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)


# Converts np.array to TEXT when inserting
sql.register_adapter(np.ndarray, adaptArray)

# Converts TEXT to np.array when selecting
sql.register_converter("array", convertArray)

def dbCreate():
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS database(Id INTEGER PRIMARY KEY, Name TEXT, Data array, Dist REAL, Pass INTEGER)")
    con.commit()
    con.close()

def dbCreate1():
    con = sql.connect('Datab.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS database(Id INTEGER PRIMARY KEY, Password INT)")
    con.commit()
    con.close()
    return
    
def dbInsert():
    con = sql.connect('Database.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    con.commit()
    c.execute("INSERT INTO database(Name, Data) VALUES(?,?)", (name, data))
    con.commit()
    con.close()
    return
    
def dbInsert1():
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    con.commit()
    c.execute("INSERT INTO database(Name, Data, Dist, Pass) VALUES(?,?,?,?)", (name, data, dist, pin))
    con.commit()
    con.close()
    return

def dbReadData():
    con = sql.connect('Database.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("SELECT Data FROM database")
    con.commit()
    d = np.array(c.fetchall())
    #print(d, d.shape)
    d = d.reshape(len(d), -1)
    #print(d, d.shape)
    con.commit()
    con.close()
    return d
    
def dbReadData1(name):
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    
    c.execute("SELECT Data FROM database WHERE Name = (?)",[name])
    con.commit()
    d = np.array(c.fetchone())
    d = d.reshape(len(d),-1)
    #print(d, d.shape)
    con.commit()
    con.close()
    return d    

def dbReadLabels():
    con = sql.connect('Database.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("SELECT Name FROM database")
    dl = np.array(c.fetchall())
    dl = dl.ravel()
    #print(dl, dl.shape)
    con.commit()
    con.close()
    return dl
    
def dbReadLabels1(name):
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("SELECT Name FROM database WHERE Id = 2")
    dl = c.fetchone()
    dl = dl[0]
    #print(dl)
    con.commit()
    con.close()
    return dl    

def dbReadDist(name):
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("SELECT Dist FROM database WHERE Name = (?)",[name])
    di = c.fetchone()
    di = di[0]
    #dl = dl.ravel()
    #print(di, type(di))
    con.commit()
    con.close()
    return di

def dbReadPass(id):
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("SELECT Pass FROM database WHERE id = (?)",[id])
    p = c.fetchone()
    p = p[0]
    print(p, type(p))
    con.commit()
    con.close()
    return p
    

def dbReadPass1(pin):
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("SELECT Name FROM database WHERE Pass =(?)",[pin])
    n = c.fetchone()
    n = n[0]
    con.commit()
    con.close()
    return n
     
def dbUpdateDist():
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("UPDATE database SET Dist=(?) WHERE ID = 6",[dist])
    con.commit()
    con.close()
    return

   
def dbUpdateName():
    con = sql.connect('Databas.db', detect_types=sql.PARSE_DECLTYPES)
    c = con.cursor()
    c.execute("UPDATE database SET Name=(?) WHERE ID = 6",[name])
    con.commit()
    con.close()
    return

#dbUpdateName()        
#dbCreate()
#dbCreate1()
#dbInsert()
#dbInsert1()
#dbReadData1(name)
#dbReadData()
#dbReadLabels()
#dbReadLabels1()
#dbReadDist(name)
dbUpdateDist()
#dbReadPass(id)
#dbReadPass1(pin)
