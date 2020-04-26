import sqlite3

def insertarTabla(region, paises, language, time):
    conexion = sqlite3.connect("tabla.db")
    consulta = conexion.cursor()

    for i in range(len(region)):
        argumentos = (region[i],paises[i],language[i],time[i])
        sql = """
            INSERT INTO tabla(region,paises,language,time)
            VALUES(?,?,?,?)
            """
        consulta.execute(sql,argumentos)

    consulta.close()
    conexion.commit()