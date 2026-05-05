from colorama import Fore, Style, init
from variables import cargar_configuracion, guardar_configuracion
from calculos import base_mas_excedente_parcela

# Inicializa colorama para que los colores funcionen correctamente en Windows
init(autoreset=True)

def visualizar_tabla():
    """Muestra los valores actuales del CSV en formato tabla."""
    c = cargar_configuracion()
    print("\n" + "-" * 55)
    print(f"{'PARÁMETRO':<40} | {'VALOR':>10}")
    print("-" * 55)
    for nombre, valor in c.items():
        # :<40 alinea a la izquierda, :>10.2f alinea a la derecha con 2 decimales
        print(f"{nombre:<40} | {valor:>10.2f}")
    print("-" * 55)
    input("\nPresione Enter para volver al menú...")

def editar_valores():
    """Permite al usuario modificar los valores uno por uno."""
    c = cargar_configuracion()
    nuevos_datos = {}
    print("\n" + "="*49)
    print("      EDITOR DE VALORES (CSV)")
    print("  (Presione Enter para mantener el valor actual)")
    print("="*49)

    for nombre, valor in c.items():
        entrada = input(f"{nombre} [{valor}]: ")
        if entrada.strip() == "":
            nuevos_datos[nombre] = valor
        else:
            try:
                nuevos_datos[nombre] = float(entrada)
            except ValueError:
                print(f"Valor inválido para {nombre}. Se mantiene el actual.")
                nuevos_datos[nombre] = valor
    
    guardar_configuracion(nuevos_datos)
    print("\n[!] Archivo actualizado con éxito.")
    input("Presione Enter para continuar...")

def menu_principal():
    opciones = ['1', '2', '3', '4', '5', '0']

    while True:
        print("\n" + "="*49)
        print("====== PROGRAMA PARA CÁLCULO DE HONORARIOS ======")
        print("="*49)
        print("\nMENU")
        print("-"*49)
        print(Fore.BLUE + "TRABAJOS")
        print("1. Replanteo y Amojonamiento")
        print("2. Certificación Parcelaria")
        print("3. Mensura Urbana Simple")
        print("-"*49)
        print(Fore.BLUE + "CONFIGURACIÓN")
        print("4. Visualizar tabla de valores actuales")
        print("5. Editar valores (CSV)")
        print("-"*49)
        print("0. Salir")

        opt = input("\nElija una opción: ")

        if opt not in opciones:
            print("Opción inválida, vuelva a intentar.")
            continue

        if opt == '0':
            print("\n¡Hasta luego!")
            break

        # OPCIONES DE CÁLCULO
        if opt in ['1', '2', '3']:
            # Cargamos configuración fresca antes de cada cálculo
            c = cargar_configuracion()
            
            try:
                nro_parcelas = int(input("Ingrese cantidad de parcelas: "))
                recargo = float(input("Ingrese % de recargo de honorarios: "))
                
                # Definimos qué base usar según la opción
                if opt == '1':
                    v_base = c['valor_acta_base']
                    v_parc = c['valor_acta_parcela']
                elif opt == '2':
                    v_base = c['valor_acta_certificacion_parcelaria']
                    v_parc = c['valor_acta_parcela']
                elif opt == '3':
                    v_base = c['valor_mensura_base']
                    v_parc = c['valor_mensura_parcela']

                # Realizamos el cálculo enviando el diccionario 'c' completo
                honorarios, honorarios_extra, sellado_cpam = base_mas_excedente_parcela(
                    v_base, v_parc, nro_parcelas, recargo, c
                )

                print("\n" + "-"*20)
                print("CÁLCULO RESULTANTE")
                print("-"*20)
                resultado = honorarios_extra if recargo != 0 else honorarios
                print(f"Honorarios:    ${resultado:,.2f}")
                print(f"Sellado CPAM:  ${sellado_cpam:,.2f}")
                print("-"*20)

            except ValueError:
                print("\n[!] Error: Por favor ingrese números válidos.")
            
            continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
            if continuar != 's':
                print("\n¡Chau!")
                break

        # OPCIONES DE CONFIGURACIÓN
        elif opt == '4':
            visualizar_tabla()
        
        elif opt == '5':
            editar_valores()

if __name__ == "__main__":
    menu_principal()