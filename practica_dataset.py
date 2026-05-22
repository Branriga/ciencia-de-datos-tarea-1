import numpy as np
import pandas as pd

# =========================
# CONFIGURACIÓN GENERAL
# =========================

np.random.seed(42)

TOTAL_CONSULTAS = 5000
CONSULTAS_POR_MOTOR = 2500

# Distribución de operaciones
LECTURAS = int(CONSULTAS_POR_MOTOR * 0.60)     # 1500
ESCRITURAS = int(CONSULTAS_POR_MOTOR * 0.40)   # 1000

# =========================
# DATOS FIJOS DEL ENTORNO
# =========================

hardware_cpu = "8 vCPU Intel Xeon"
hardware_ram = "32 GB RAM"
almacenamiento = "1 TB SSD"
topologia_red = "10 Gbps Ethernet"
volumen_inicial_datos = "500 GB"

# =========================
# GENERACIÓN DEL DATASET
# =========================

datos = []

motores = ["MongoDB", "Cassandra"]

for motor in motores:

    # -------------------------
    # LECTURAS
    # -------------------------
    for _ in range(LECTURAS):

        if motor == "MongoDB":
            tiempo = np.random.normal(11, 4)
            cpu = np.random.normal(55, 8)
        else:
            tiempo = np.random.normal(10, 3)
            cpu = np.random.normal(45, 6)

        datos.append({
            "motor_bd": motor,
            "tipo_operacion": "Lectura",
            "tiempo_respuesta_ms": round(max(tiempo, 1), 2),
            "uso_cpu_porcentaje": round(max(cpu, 1), 2),
            "tamano_carga_kb": round(np.random.uniform(5, 300), 2),
            "hardware_cpu": hardware_cpu,
            "hardware_ram": hardware_ram,
            "almacenamiento": almacenamiento,
            "topologia_red": topologia_red,
            "volumen_inicial_datos": volumen_inicial_datos
        })

    # -------------------------
    # ESCRITURAS
    # -------------------------
    for _ in range(ESCRITURAS):

        if motor == "MongoDB":
            tiempo = np.random.normal(18.2, 8.5)
            cpu = np.random.normal(60, 10)
        else:
            tiempo = np.random.normal(12.5, 4.2)
            cpu = np.random.normal(48, 7)

        datos.append({
            "motor_bd": motor,
            "tipo_operacion": "Escritura",
            "tiempo_respuesta_ms": round(max(tiempo, 1), 2),
            "uso_cpu_porcentaje": round(max(cpu, 1), 2),
            "tamano_carga_kb": round(np.random.uniform(10, 500), 2),
            "hardware_cpu": hardware_cpu,
            "hardware_ram": hardware_ram,
            "almacenamiento": almacenamiento,
            "topologia_red": topologia_red,
            "volumen_inicial_datos": volumen_inicial_datos
        })

# =========================
# CREAR DATAFRAME
# =========================

df = pd.DataFrame(datos)

# =========================
# VALIDACIONES
# =========================

print("Total de registros:", len(df))
print("\nConsultas por motor:")
print(df["motor_bd"].value_counts())

print("\nDistribución de operaciones:")
print(df["tipo_operacion"].value_counts())

print("\nPrimeras filas del dataset:")
print(df.head())

# =========================
# EXPORTAR CSV
# =========================

df.to_csv("dataset_nosql_controlado.csv", index=False)

print("\nDataset generado correctamente.")
print("Archivo guardado como: dataset_nosql_controlado.csv")