import pandas as ad
import numpy as np
import matplotlib.pyplot as plt

#carga de archivos
df = pd.read_csv("ventas_productos.csv")

#mostrar los primeros registros
print ("Primeros registros del dataset:")
print (df.head())

#funcion para calcular el precio total
def calcular_precio_total (cantidad,precio):
    return cantidad*precio

#aplicar la función al dataframe
df["Precio_total"] = df.apply(lambda row: calcular_precio_total (row [cantidad], row [precio]), axis 1)

#mostrar el dataframe con el precio total
print ("\nDataFrame con el precio total")