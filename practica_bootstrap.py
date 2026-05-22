import numpy as np
import pandas as pd

# 1. Simulación de los datos de entrada (basado en la descripción del problema)
# En un entorno real, esto sería: df = pd.read_csv('datos_rendimiento_nosql.csv')
# Aquí generamos datos representativos para que el código sea ejecutable
np.random.seed(42)
n_escrituras = 1000

# Simulamos tiempos de respuesta con asimetría positiva (usando distribución log-normal)
tiempos_cassandra = np.random.lognormal(mean=2.45, sigma=0.3, size=n_escrituras) # Media ~ 12.5 ms
tiempos_mongo = np.random.lognormal(mean=2.80, sigma=0.4, size=n_escrituras)     # Media ~ 18.2 ms

# 2. Configuración de los parámetros del Bootstrap
B = 2000 # Número de réplicas Bootstrap
diferencias_medias = np.zeros(B)

# 3. Bucle iterativo de remuestreo (Bootstrap)
for i in range(B):
    # a. Extraer muestras con reemplazo del mismo tamaño que las originales
    muestra_boot_mongo = np.random.choice(tiempos_mongo, size=n_escrituras, replace=True)
    muestra_boot_cassandra = np.random.choice(tiempos_cassandra, size=n_escrituras, replace=True)
    
    # b. Calcular la métrica de interés para esta iteración (Diferencia de Medias)
    media_mongo_boot = np.mean(muestra_boot_mongo)
    media_cassandra_boot = np.mean(muestra_boot_cassandra)
    
    # c. Almacenar el resultado en el arreglo
    diferencias_medias[i] = media_mongo_boot - media_cassandra_boot

# 4. Cuantificación de la Incertidumbre (Cálculo del Intervalo de Confianza)
# Se calculan los percentiles 2.5% y 97.5% de la distribución de diferencias
limite_inferior = np.percentile(diferencias_medias, 2.5)
limite_superior = np.percentile(diferencias_medias, 97.5)
error_estandar_boot = np.std(diferencias_medias)

# 5. Salida de resultados
print("=== RESULTADOS DEL REMUESTREO BOOTSTRAP ===")
print(f"Iteraciones (B): {B}")
print(f"Diferencia de Medias Observada: {np.mean(tiempos_mongo) - np.mean(tiempos_cassandra):.2f} ms")
print(f"Error Estándar (Bootstrap): {error_estandar_boot:.2f} ms")
print(f"Intervalo de Confianza al 95%: [{limite_inferior:.2f} ms , {limite_superior:.2f} ms]")