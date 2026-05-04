from calculos import replanteo_y_amojonamiento

opciones = [1,2,3,0]

while True:

    print ("\n" + "="*49)
    print ("====== PROGRAMA PARA CÁLCULO DE HONORARIOS ======")
    print ("="*49)
    print ("\nMENU")
    print ("-"*49)
    print ("ACTAS DE AMOJONAMIENTOS")
    print ("1. Replanteo y amojonamiento")
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
                honorarios, honorarios_extra, sellado_cpam = replanteo_y_amojonamiento(nro_parcelas, recargo)
                if recargo != 0:
                    #print (type(honorarios_extra))
                    print (f"\nHonorarios: ${honorarios_extra}")
                    print (f"Sellado CPAM: ${sellado_cpam}")
                    break
                else:
                    print (f"\nHonorarios: ${honorarios}")
                    print (f"Sellado CPAM: ${sellado_cpam}")
                    break
            except ValueError:
                print ("Valor incorrecto")

        continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").lower()
        if continuar != 's':
            print("Gracias por usar el programa.")
            break
