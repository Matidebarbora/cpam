from calculos import replanteo_y_amojonamiento

opciones = [1,2,3]

print ("\n" + "="*49)
print ("====== PROGRAMA PARA CÁLCULO DE HONORARIOS ======")
print ("="*49)
print ("\nMENU")
print ("\nACTAS DE AMOJONAMIENTOS")
print ("1. Replanteo y amojonamiento")

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

if (opt == 1):
    while True:
        try:
            nro_parcelas = int(input("Ingrese cantidad de parcelas: "))
            recargo = int(input("Ingrese % de recargo de honorarios: "))
            honorarios, honorarios_extra, sellado_cpam = replanteo_y_amojonamiento(nro_parcelas, recargo)
            #print (type(honorarios))
            print (f"\nHonorarios: ${honorarios}")
            if recargo != 0:
                #print (type(honorarios_extra))
                print (f"Honorarios + {recargo}%: ${honorarios_extra}")
                break
            else:
                break
        except ValueError:
            print ("Valor incorrecto")

