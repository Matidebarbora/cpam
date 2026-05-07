import os
import time
import csv
from colorama import Fore, Style, init
from variables import cargar_configuracion, guardar_configuracion_completa
from calculos import base_mas_excedente_parcela, mensura_con_fraccionamiento

init(autoreset=True)

ind4 = "    "
ind8 = "        "

NARANJA = '\033[38;5;214m'
MAGENTA = '\033[38;5;201m'

def formato_moneda(valor):
    temp = f"{valor:,.2f}"
    return temp.replace(',', 'X').replace('.', ',').replace('X', '.')

def gestionar_configuracion():
    """
    Muestra la tabla y permite decidir si editar o salir.
    """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            with open('valores.csv', mode='r', encoding='utf-8') as f:
                datos = list(csv.DictReader(f))
            
            # Encabezados con alineación corregida (| {i:<2} | para evitar desfases)
            header = f"| #  | {'DESCRIPCIÓN':<45} | {'VALOR':>15} |"
            separator = f"|----|{'-'*47}|{'-'*17}|"
            
            print(f"\n{header}")
            print(separator)
            
            for i, fila in enumerate(datos, 1):
                v_formateado = formato_moneda(float(fila['valor']))
                # El :<2 asegura que los números de 2 dígitos no muevan la tabla
                print(f"| {i:<2} | {fila['descripcion']:<45} | {NARANJA}{v_formateado:>15}{Style.RESET_ALL} |")
            
            print(f"{separator}\n")
            
            accion = input(f"Pulse [{Fore.CYAN}M{Style.RESET_ALL}] para modificar un valor o [{Fore.CYAN}Enter{Style.RESET_ALL}] para volver: ").lower()
            
            if accion == 'm':
                try:
                    idx_in = input("\nIndique el número (#) a modificar: ")
                    idx = int(idx_in) - 1
                    if 0 <= idx < len(datos):
                        seleccionado = datos[idx]
                        print(f"\nEditando: {Fore.CYAN}{seleccionado['descripcion']}{Style.RESET_ALL}")
                        nuevo_val = input(f"Valor actual ({formato_moneda(float(seleccionado['valor']))}). Nuevo: ")
                        if nuevo_val.strip() != "":
                            datos[idx]['valor'] = float(nuevo_val.replace(',', '.'))
                            guardar_configuracion_completa(datos)
                            print(f"{Fore.GREEN}[!] Actualizado.{Style.RESET_ALL}")
                            time.sleep(1)
                    else:
                        print(f"{Fore.RED}Número fuera de rango.{Style.RESET_ALL}")
                        time.sleep(1)
                except ValueError:
                    print(f"{Fore.RED}Entrada inválida.{Style.RESET_ALL}")
                    time.sleep(1)
            else:
                break # Vuelve al menú principal
        except FileNotFoundError:
            print(f"{Fore.RED}Error: No se encontró valores.csv{Style.RESET_ALL}")
            input("Presione Enter para volver...")
            break

def menu_principal():
    # Eliminamos 'E' de las opciones, dejamos solo 'R'
    opciones = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'R', 'Q']

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*49)
        print("====== PROGRAMA PARA CÁLCULO DE HONORARIOS ======")
        print("="*49)
        print("\nMENU")
        print("-"*49)
        print(Fore.BLUE + "TRABAJOS")
        print("-"*49)
        print("ACTA DE AMOJONAMIENTO")
        print(ind4 + "1.  Replanteo y Amojonamiento")
        print(ind8 + "Acta de amojonamiento baldío / edificado")
        print(ind4 + "2.  Certificación Parcelaria")
        print(ind4 + "3.  Acta de amojonamiento de sector de obra (próximamente)")
        print("-"*49)
        print("MENSURA")
        print(ind4 + "4.  Mensura simple urbana")
        print(ind8 + "Servidumbre / Superficie / Unificación")
        print("-"*49)
        print("MENSURA CON FRACCIONAMIENTO")
        print(ind4 + "5.  Mensura de 2 a 120 parcelas")
        print("-"*49)
        print(Fore.BLUE + "CONFIGURACIÓN")
        print(ind4 + "R. Ver tabla de variables / Modificar")
        print("-"*49)
        print(Fore.RED + "Q. Salir")

        opt = input("\nElija una opción: ").upper()

        if opt not in opciones:
            print(Fore.RED + "Opción inválida.")
            time.sleep(1)
            continue

        if opt == 'Q':
            print("\n¡Hasta luego!")
            input("Presione Enter para salir...")
            break

        if opt == 'R':
            gestionar_configuracion()
            continue

        if opt in ['1', '2', '4', '5']:
            c = cargar_configuracion()
            try:
                if opt == '1':
                    nro = int(input("\nIngrese cantidad de parcelas: "))
                    rec_in = input("Ingrese % de recargo (Enter para 0): ")
                    rec = float(rec_in.replace(',', '.')) if rec_in.strip() != "" else 0
                    v_b, v_p, v_c = c['v_acta_base'], c['v_acta_parcela'], c['v_ajuste_cpam']
                    h, he, sel = base_mas_excedente_parcela(v_b, v_p, nro, rec, c, v_c)
                    res = he if rec != 0 else h
                    print("\n" + "-"*30 + f"\nHonorarios: {NARANJA}${formato_moneda(res)}{Style.RESET_ALL}\nSellado CPAM: {NARANJA}${formato_moneda(sel)}{Style.RESET_ALL}\n" + "-"*30)

                elif opt == '2':
                    nro = int(input("\nIngrese cantidad de parcelas: "))
                    rec_in = input("Ingrese % de recargo (Enter para 0): ")
                    rec = float(rec_in.replace(',', '.')) if rec_in.strip() != "" else 0
                    v_b, v_p, v_c = c['v_acta_base'], c['v_acta_parcela'], c['v_ajuste_cpam']
                    h, he, sel = base_mas_excedente_parcela(v_b, v_p, nro, rec, c, v_c)
                    res = he if rec != 0 else h
                    print("\n" + "-"*30 + f"\nHonorarios: {NARANJA}${formato_moneda(res)}{Style.RESET_ALL}\nSellado CPAM: {NARANJA}${formato_moneda(sel)}{Style.RESET_ALL}\n" + "-"*30)

                elif opt == '4':
                    nro = int(input("\nIngrese cantidad de parcelas: "))
                    rec_in = input("Ingrese % de recargo (Enter para 0): ")
                    rec = float(rec_in.replace(',', '.')) if rec_in.strip() != "" else 0
                    v_b, v_p, v_c = c['v_acta_base'], c['v_acta_parcela'], c['v_ajuste_cpam']
                    h, he, sel = base_mas_excedente_parcela(v_b, v_p, nro, rec, c, v_c)
                    res = he if rec != 0 else h
                    print("\n" + "-"*30 + f"\nHonorarios: {NARANJA}${formato_moneda(res)}{Style.RESET_ALL}\nSellado CPAM: {NARANJA}${formato_moneda(sel)}{Style.RESET_ALL}\n" + "-"*30)

                elif opt == '5':
                    nro_t = int(input("\nIngrese cantidad TOTAL de parcelas: "))
                    nro_e = int(input("Ingrese cantidad de parcelas EDIFICADAS: "))
                    rec_in = input("Ingrese % de recargo (Enter para 0): ")
                    rec = float(rec_in.replace(',', '.')) if rec_in.strip() != "" else 0
                    h, he, sel = mensura_con_fraccionamiento(nro_t, nro_e, rec, c)
                    res = he if rec != 0 else h
                    print("\n" + "-"*30 + f"\nHonorarios: {NARANJA}${formato_moneda(res)}{Style.RESET_ALL}\nSellado CPAM: {NARANJA}${formato_moneda(sel)}{Style.RESET_ALL}\n" + "-"*30)

                input("\nPresione Enter para continuar...")
            except ValueError:
                print(Fore.RED + "\n[!] Error: Ingrese números válidos.")
                time.sleep(1)

if __name__ == "__main__":
    try:
        menu_principal()
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
        input("Presione Enter para cerrar...")