import pandas as pd
from mysql.connector import connect, Error

class Migracion1:
    def __init__(self,host,user,password,database,df):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.conexion=None
        self.df=df

    def conectar_servidor(self):
        try:
            self.conexion=connect(host=self.host,user=self.user,password=self.password)
            if self.conexion:
                print("Conexion Exitosa")
        except Error as e:
            print(e)

    def desconectar(self):
            self.conexion.close()

    def crear_database(self):
        if self.conexion:
            try:
                cursor=self.conexion.cursor()
                sql= f"CREATE DATABASE IF NOT EXISTS `{self.database}`"
                cursor.execute(sql,)
                print("Base de datos creada")
                cursor.close()
                self.desconectar()

            except Error as e:
                print(e)

    def conectar_database(self):
        try:
          self.conexion = connect(host=self.host, user=self.user, password=self.password,database=self.database)
          if self.conexion:
              print("Conectado a la base de datos")

        except Error as e:
            print(e)

    def crear_tabla(self):
        try:
            cursor=self.conexion.cursor()
            sql="Create table if not exists Peliculas (nombre varchar(255),estreno date,director varchar(255),calificacion float, genero varchar (255),duracion varchar(255))"
            cursor.execute(sql,)
            cursor.close()

        except Error as e:
            print(e)

    def insertar_data(self):
        if self.conexion:
            try:
                cursor = self.conexion.cursor()
                for index, row in self.df.iterrows():
                    sql= "INSERT INTO Peliculas(nombre,estreno,director,calificacion,genero,duracion) VALUES(%s,%s,%s,%s,%s,%s);"
                    valores=(row["nombre"],row["estreno"],row["director"],row["calificacion"],row["genero"],row["duracion"])
                    cursor.execute(sql,valores)
                self.conexion.commit()
                cursor.close()
                self.desconectar()
            except Error as e:
                print(e)


if __name__=="__main__":
    df=pd.read_csv("DATA/Df_Peliculas_Limpio")
    password = "Bairon179"
    migracion=Migracion1("localhost","root",password,"cinema_bd",df)
    migracion.conectar_servidor()
    migracion.crear_database()
    migracion.conectar_database()
    migracion.crear_tabla()
    migracion.insertar_data()

