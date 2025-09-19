
import numpy as np
import pandas as pd
import time


num_alumnos = 1000   
num_materias = 100   


datos_calificaciones = np.random.randint(5, 11, size=(num_alumnos, num_materias))


indice_alumnos = [f'Alumno_{i+1}' for i in range(num_alumnos)]
nombres_materias = [f'Materia_{i+1}' for i in range(num_materias)]

df_calificaciones = pd.DataFrame(datos_calificaciones, 
                                 index=indice_alumnos, 
                                 columns=nombres_materias)


print("Vista rápida de la tabla (primeras 5 filas):")
print(df_calificaciones.head())
print("\n" + "="*50 + "\n")


alumno_a_buscar = 'Alumno_321'
materia_a_buscar = 'Materia_5'

try:
    calificacion_encontrada = df_calificaciones.loc[alumno_a_buscar, materia_a_buscar]
    print(f"Calificación de {alumno_a_buscar} en {materia_a_buscar}: {calificacion_encontrada}")
except KeyError:
    print("El alumno o la materia no se encontró en la tabla.")


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print("\nMostrando toda la tabla:")
start = time.time()
print(df_calificaciones)
end = time.time()

print(f"\nTiempo en imprimir la tabla completa: {end - start:.2f} segundos")
