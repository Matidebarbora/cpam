import csv

def cargar_configuracion():
    config = {}
    try:
        with open('valores.csv', mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                config[fila['nombre']] = float(fila['valor'])
    except FileNotFoundError:
        return {} # Manejar valores por defecto aquí si se desea
    return config

def guardar_configuracion_completa(lista_filas):
    with open('valores.csv', mode='w', newline='', encoding='utf-8') as f:
        campos = ['nombre', 'valor', 'descripcion']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista_filas)
