import csv

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
            "v_agrim": 300, "v_autoconsulta": 600, "v_geofada": 720,
            "v_matricula": 5, "v_acta_base": 388800, "v_acta_parcela": 48000,
            "v_acta_cert_parcel": 500000, "v_mensura_base": 648000,
            "v_mensura_parcela": 130000
        }
    return config

def guardar_configuracion(diccionario_datos):
    with open('valores.csv', mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=['nombre', 'valor'])
        escritor.writeheader()
        for nombre, valor in diccionario_datos.items():
            escritor.writerow({'nombre': nombre, 'valor': valor})
