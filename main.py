from colorama import Fore, Style, init
from variables import valor_acta_base, valor_acta_parcela, valor_mensura_base, valor_mensura_parcela, valor_acta_certificacion_parcelaria
from calculos import base_mas_excedente_parcela


opciones = [1,2,3,0]

while True:

    print ("\n" + "="*49)
    print ("====== PROGRAMA PARA CÁLCULO DE HONORARIOS ======")
    print ("="*49)
    print ("\nMENU")
    print ("-"*49)
    print (Fore.BLUE + "ACTA DE AMOJONAMIENTO")
    print (Style.RESET_ALL)
    print ("1. Replanteo y amojonamiento")
    print ("   Acta de amojonamiento baldío")
    print ("   Acta de amojonamiento edificado")
    print ("2. Certificación parcelaria")
    print ("-"*49)
    print (Fore.BLUE + "MENSURA")
    print (Style.RESET_ALL)
    print ("3. Mensura simple Urbana")
    print ("   Mensura para derecho real de servidumbre")
    print ("   Mensura para derecho real de superficie")
    print ("   Mensura con unificación")
    print ("-"*49)
    print ("0. Salir")

    opt = None

    while True:
        try:
            entrada = int(input("\nElija una opción: "))
            if entrada in opciones:
                opt = entrada
                break
            else:
                print ("Opción inválida, vuelva a intentar")
        except ValueError:
            print ("Opción inválida, vuelva a intentar")

    if opt == 0:
        print("\n¡Hasta luego!")
        break
    
    if (opt == 1):
        while True:
            try:
                nro_parcelas = int(input("Ingrese cantidad de parcelas: "))
                recargo = int(input("Ingrese % de recargo de honorarios: "))
                honorarios, honorarios_extra, sellado_cpam = base_mas_excedente_parcela(valor_acta_base, valor_acta_parcela, nro_parcelas, recargo)
                print ("\nCÁLCULO")
                if recargo != 0:
                    #print (type(honorarios_extra))
                    print (f"\nHonorarios: ${honorarios_extra:.2f}")
                    print (f"Sellado CPAM: ${sellado_cpam:.2f}")
                    break
                else:
                    print (f"\nHonorarios: ${honorarios:.2f}")
                    print (f"Sellado CPAM: ${sellado_cpam:.2f}")
                    break
            except ValueError:
                print ("Valor incorrecto")

        continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if continuar != 's':
            print("\nChau potolino")
            break

    if (opt == 2):
        while True:
            try:
                nro_parcelas = int(input("Ingrese cantidad de parcelas: "))
                recargo = int(input("Ingrese % de recargo de honorarios: "))
                honorarios, honorarios_extra, sellado_cpam = base_mas_excedente_parcela(valor_acta_certificacion_parcelaria, valor_acta_parcela, nro_parcelas, recargo)
                print ("\nCÁLCULO")
                if recargo != 0:
                    #print (type(honorarios_extra))
                    print (f"\nHonorarios: ${honorarios_extra:.2f}")
                    print (f"Sellado CPAM: ${sellado_cpam:.2f}")
                    break
                else:
                    print (f"\nHonorarios: ${honorarios:.2f}")
                    print (f"Sellado CPAM: ${sellado_cpam:.2f}")
                    break
            except ValueError:
                print ("Valor incorrecto")

        continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if continuar != 's':
            print("\nChau potolino")
            break

    if (opt == 3):
        while True:
            try:
                nro_parcelas = int(input("Ingrese cantidad de parcelas: "))
                recargo = int(input("Ingrese % de recargo de honorarios: "))
                honorarios, honorarios_extra, sellado_cpam = base_mas_excedente_parcela(valor_mensura_base, valor_mensura_parcela, nro_parcelas, recargo)
                print ("\nCÁLCULO")
                if recargo != 0:
                    #print (type(honorarios_extra))
                    print (f"\nHonorarios: ${honorarios_extra:.2f}")
                    print (f"Sellado CPAM: ${sellado_cpam:.2f}")
                    break
                else:
                    print (f"\nHonorarios: ${honorarios:.2f}")
                    print (f"Sellado CPAM: ${sellado_cpam:.2f}")
                    break
            except ValueError:
                print ("Valor incorrecto")

        continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if continuar != 's':
            print("\nChau potolino")
            break