import csv

# --- General ------------------------
valor_agrim = 300
valor_autoconsulta = 600
valor_geofada = 720
valor_matricula = 5 # expresado en %. Es el porcentaje que retiene el colegio.

# ---- Acta de amojonamiento ----------
valor_acta_base = 388800
valor_acta_parcela = 48000
valor_acta_certificacion_parcelaria = 500000
valor_acta_sector_obra = 333000

# ---- Mensura -----------------------
valor_mensura_base = 648000
valor_mensura_parcela = 130000

def cargar_configuracion():
    config = {}
    try:
        with open('valores.csv', mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                config[fila['nombre']] = float(fila['valor'])
    except FileNotFoundError:
        # Valores por defecto por si el archivo no existe aún
        return {
            "valor_agrim": 300, "valor_autoconsulta": 600, "valor_geofada": 720,
            "valor_matricula": 5, "valor_acta_base": 388800, "valor_acta_parcela": 48000,
            "valor_acta_certificacion_parcelaria": 500000, "valor_mensura_base": 648000,
            "valor_mensura_parcela": 130000
        }
    return config

def guardar_configuracion(diccionario_datos):
    with open('valores.csv', mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=['nombre', 'valor'])
        escritor.writeheader()
        for nombre, valor in diccionario_datos.items():
            escritor.writerow({'nombre': nombre, 'valor': valor})
