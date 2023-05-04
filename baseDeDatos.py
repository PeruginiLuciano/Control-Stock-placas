import sqlite3 as sql

def crearDb():
    conn = sql.connect("StockPlacas.db")
    conn.commit()
    conn.close()

def createTabla():
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE StockPlaca (
            Nombre text,
            Modelo text,
            Versión text,
            Precio text,
            Fecha text,
            Total integer,
            Estado text
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre,modelo,version,precio,fecha,total,estado):
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO StockPlaca VALUES ('{nombre}','{modelo}','{version}','{precio}','{fecha}',{total},'{estado}')"
    cursor.execute(instruccion)
    
    conn.commit()
    conn.close()
    

def insertRows(streamerList):
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?,?,?)"
    cursor.executemany(instruccion,streamerList)
    
    conn.commit()
    conn.close()

def readRow():
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM StockPlaca"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def readOrdered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search(field):
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM StockPlaca WHERE Nombre like '{field}%'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(len(datos))
    return(datos)

def searchAll():
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM StockPlaca "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print (datos)
    return datos

def updateField(name,field):
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE StockPlaca SET Estado='{field}' WHERE Nombre = '{name}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

def updateFields(edit,name,field):
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE StockPlaca SET '{edit}'='{field}' WHERE Nombre = '{name}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()


def deleteRow(field):
    conn = sql.connect("StockPlacas.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM StockPlaca WHERE Nombre ='{field}' "
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    #crearDb()
    #createTabla()
    #insertRow("Andres",700,2)
    #insertRow("Ale",7000,20)
    #insertRow("Robert",70,200)
    #readRow()
    #streamers = [("Hola",100000000,1),("Chau",1202,15),("RERA",456,4)]
    #readOrdered("NAME")
    #insertRows(streamers)
    #updateFields()
    pass