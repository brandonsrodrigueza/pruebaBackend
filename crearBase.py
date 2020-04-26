import sqlite3

def crearBase():
    conexion = sqlite3.connect('tabla.db')
    consulta = conexion.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS tabla(
        region text NOT NULL,
        paises  text Name NOT NULL,
        language text NOT NULL,
        time text NOT NULL)
    """
    if(consulta.execute(sql)):
        print("Tabla creada")
    else: print("Error de creación")

    consulta.close()

    conexion.commit()

    conexion.close()

