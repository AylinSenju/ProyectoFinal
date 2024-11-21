import pandas as pd


#Esta funcion ayuda a detectar cuanto porcentaje se tiene de valores nulos dentro de el df,
#la idea es saber si se recolectaron bien los datos
def porcentaje_nulos(df):
    nulos = df.isnull().sum()
    total = len(df)
    porcentaje = (nulos / total)*100

    return porcentaje


#Busca las columnas con valores nulos y ve si sobrepasan la media de valores nulos
#en caso de ser asi, elimina la fila
def columnas_nulos(df,porcentaje):
    if porcentaje<0 or porcentaje>1:
        print("ERROR: El porcentaje debe ser entre 0 y 1")
        return

    porcentaje_nulos = df.isnull().mean()
    columnas_a_eliminar= []

    for columna, porcentaje_nulo in porcentaje_nulos.items():
        if porcentaje_nulo >= porcentaje:
            columnas_a_eliminar.append(columna)
    df.drop(columns=columnas_a_eliminar, inplace= True)


    return columnas_a_eliminar


#Busca los renglones duplicados y los cuenta para poder saber cuantos datos duplicados se tiene dentro
#del df oririginal
def duplicados_renglones(df):
    duplicados =df.duplicated().sum()
    return duplicados


#Elimina los datos duplicados del datframre
def eliminar_repetidos(df):
    df.drop_duplicates(inplace = True)
    duplicados = len(df.drop_duplicates())
    total = len(df)
    eliminados = total-duplicados
    return f"Los renglones eliminados que son duplicados fueron {eliminados}"





if __name__ == "__main__":
    dataframe_Peliculas = pd.read_csv("DATA/Df_Peliculas")
    dataframe_Series = pd.read_csv("DATA/Df_Series")


    porcentaje_de_nulos_Series = porcentaje_nulos(dataframe_Series)
    porcentaje_de_nulos_Peliculas = porcentaje_nulos(dataframe_Series)

    print("El porcentaje de nulos de Df de Series es de: ",porcentaje_de_nulos_Series)
    print("El porcentaje de nulos de Df de Peliculas es de: ",porcentaje_de_nulos_Peliculas)

    print("/////////////////////////////////////////////////////////////////\n")


    duplicados_Series = duplicados_renglones(dataframe_Series)
    duplicados_Peliculas = duplicados_renglones(dataframe_Peliculas)
    print("La cantidad de duplicados del dataframe de Series fue de: ", duplicados_Series)
    print("La cantidad de duplicados del dataframe de Peliculas fue de: ", duplicados_Peliculas)


    #En caso de que los duplicados sean mayores a 0 pues se eliminaran del datafrae original
    if duplicados_Series > 1:
        eliminar_repetidos(duplicados_Series)
    if duplicados_Peliculas >1:
        eliminar_repetidos(duplicados_Peliculas)

    print("/////////////////////////////////////////////////////////////////\n")

    columnas_eliminar_Series = columnas_nulos(dataframe_Series, 0.40)
    columnas_eliminar_Peliculas = columnas_nulos(dataframe_Peliculas, 0.40)

    print("Las columnas  eliminadas de Series fueron: ",columnas_eliminar_Series)
    print("Las columnas a eliminar de Peliculas fueron: ",columnas_eliminar_Peliculas)



    dataframe_Series.to_csv("DATA/Df_Series_Limpio")
    dataframe_Peliculas.to_csv("DATA/Df_Peliculas_Limpio")




