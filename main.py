import os
import sys
import time
from colorama import Fore, Style, init
from variables import cargar_configuracion, guardar_configuracion
from calculos import base_mas_excedente_parcela

init(autoreset=True)

NARANJA = '\033[38;5;214m'

def formato_moneda(valor):
    """
    Convierte un número al formato: 1.234.567,89
    Usa un truco de reemplazo: primero formatea a estilo inglés (comma miles, dot decimal),
    luego intercambia los signos.
    """
    # Formateamos con comas para miles y punto para decimal
    temp = f"{valor:,.2f}"
    # Intercambiamos los signos: , por X, . por ,, X por .
    return temp.replace(',', 'X').replace('.', ',').replace('X', '.')

def visualizar_tabla():
    c = cargar_configuracion()
    print("\n" + "-" * 55)
    print(f"{'PARÁMETRO':<40} | {'VALOR':>10}")
    print("-" * 55)
    for nombre, valor in c.items():
        # Visualización de la tabla también con formato prolijo
        valor_str = formato_moneda(valor)
        print(f"{nombre:<40} | {NARANJA}{valor_str:>10}{Style.RESET_ALL}")
    print("-" * 55)
    input("\nPresione Enter para volver al menú...")

def editar_valores():
    c = cargar_configuracion()
    nuevos_datos = {}
    print("\n" + "="*49)
    print("      EDITOR DE VALORES (CSV)")
    print("  (Use punto o coma, el programa lo entenderá)")
    print("="*49)

    for nombre, valor in c.items():
        valor_str = formato_moneda(valor)
        entrada = input(f"{nombre} [{NARANJA}{valor_str}{Style.RESET_ALL}]: ")
        if entrada.strip() == "":
            nuevos_datos[nombre] = valor
        else:
            try:
                # REEMPLAZO: Si tus padres ponen coma, lo pasamos a punto para que Python calcule
                entrada_limpia = entrada.replace(',', '.')
                nuevos_datos[nombre] = float(entrada_limpia)
            except ValueError:
                print(f"Valor inválido. Se mantiene el actual.")
                nuevos_datos[nombre] = valor
    
    guardar_configuracion(nuevos_datos)
    print("\n[!] Archivo actualizado con éxito.")
    input("Presione Enter para continuar...")

def menu_principal():
    opciones = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'R', 'E', 'Q']

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n" + "="*49)
        print("====== PROGRAMA PARA CÁLCULO DE HONORARIOS ======")
        print("="*49)
        print("\nMENU")
        print("-"*49)
        print(Fore.BLUE + "TRABAJOS")
        print("-"*49)
        print(Fore.MAGENTA + "ACTA DE AMOJONAMIENTO")
        print("1.  Replanteo y Amojonamiento")
        print("    Acta de amojonamiento baldío")
        print("    Acta de amojonamiento edificado")
        print("2.  Certificación Parcelaria")
        print("3.  Acta de amojonamiento de sector de obra")
        print("-"*49)
        print(Fore.MAGENTA + "MENSURA")
        print("4.  Mensura simple urbana")
        print("    Mensura para derecho real de servidumbre")
        print("    Mensura para derecho real de superficie")
        print("    Mensura con unificación")
        print("-"*49)
        print(Fore.MAGENTA + "MENSURA CON FRACCIONAMIENTO")
        print("5.  Mensura de 2 a 120 parcelas")
        print("-"*49)
        print(Fore.MAGENTA + "CONJUNTO INMOBILIARIO")
        print("6.  Conjunto inmobiliario")
        print("-"*49)
        print(Fore.MAGENTA + "MENSURA EN PROPIEDAD HORIZONTAL")
        print("7.  PH según cantidad de unidades funcionales")
        print("-"*49)
        print(Fore.MAGENTA + "MENSURA RURAL")
        print("8.  Cálculo según cantidad de hectáreas")
        print("-"*49)
        print(Fore.MAGENTA + "NIVELACIÓN GEOMÉTRICA")
        print("9.  Nivelación geométrica")
        print("10. Colocación PF (c/coord. y monogr.)")
        print("-"*49)
        print(Fore.MAGENTA + "RELEVAMIENTO PLANIMÉTRICO")
        print("11. Levantamiento planimétrico por cantidad de hectareas")
        print("-"*49)
        print(Fore.MAGENTA + "CÁLCULOS VARIOS")
        print("12. Consulta y asesoría")
        print("13. Georreferenciación parcelaria")
        print("14. Día de campo")
        print("14. Apertura de rumbo y desmonte")
        print("-"*49)
        print(Fore.BLUE + "CONFIGURACIÓN")
        print("R. Visualizar tabla de valores actuales")
        print("E. Editar valores (CSV)")
        print("-"*49)
        print(Fore.RED + "Q. Salir")

        opt = input("\nElija una opción: ")

        if opt not in opciones:
            print(Fore.RED + "Opción inválida, vuelva a intentar.")
            time.sleep(1)
            continue

        if opt == 'Q':
            print("\n¡Hasta luego!")
            input("Presione Enter para salir...")
            break

        if opt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'R', 'E', 'Q']:
            c = cargar_configuracion()
            try:
                nro_parcelas = int(input("\nIngrese cantidad de parcelas: "))
                recargo_in = input("Ingrese % de recargo (Enter para 0): ")
                
                # Manejo de coma en el recargo
                recargo = float(recargo_in.replace(',', '.')) if recargo_in.strip() != "" else 0
                
                if opt == '1':
                    v_base, v_parc = c['valor_acta_base'], c['valor_acta_parcela']
                elif opt == '2':
                    v_base, v_parc = c['valor_acta_certificacion_parcelaria'], c['valor_acta_parcela']
                else:
                    v_base, v_parc = c['valor_mensura_base'], c['valor_mensura_parcela']

                h, hextra, sellado = base_mas_excedente_parcela(v_base, v_parc, nro_parcelas, recargo, c)

                print("\n" + "-"*30)
                print(Fore.GREEN + "CÁLCULO RESULTANTE")
                print("-"*30)
                
                resultado = hextra if recargo != 0 else h
                
                # RESULTADOS EN NARANJA Y FORMATO LATINO
                print(f"Honorarios:    {NARANJA}${formato_moneda(resultado)}{Style.RESET_ALL}")
                print(f"Sellado CPAM:  {NARANJA}${formato_moneda(sellado)}{Style.RESET_ALL}")
                print("-"*30)

            except ValueError:
                print(Fore.RED + "\n[!] Error: Ingrese números válidos.")
            
            continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
            if continuar != 's': break

        elif opt == 'R':
            visualizar_tabla()
        
        elif opt == 'E':
            editar_valores()

if __name__ == "__main__":
    try:
        menu_principal()
    except Exception as e:
        # En caso de error crítico, el .exe no se cerrará sin que puedan leer qué pasó
        print(f"\nOcurrió un error inesperado: {e}")
        input("Presione Enter para cerrar...")