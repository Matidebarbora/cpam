# ----------- VALORES BASES ---------------------------------------
valor_base_acta = 388800
valor_parcela = 48000
valor_certificacion_parcelaria = 500000
valor_actar_sector_obra = 333000
valor_agrim = 300
valor_autoconsulta = 600
valor_geofada = 720
valor_matricula = 5 # expresado en %. Es el porcentaje que retiene el colegio.

# ----------- VARIABLES -------------------------------------------
nro_parcelas = int(input("Ingrese cantidad de parcelas: "))
recargo = int(input("Ingrese % de recargo de honorarios: "))

def replanteo_y_amojonamiento (nro_parcelas):
    
    honorarios = (valor_base_acta + valor_parcela) + ((nro_parcelas - 1) * valor_parcela)
    retenciones_cpam = round(((honorarios * (valor_matricula / 100) + valor_autoconsulta + valor_geofada) / valor_agrim), 0)
    sellado_cpam = retenciones_cpam * valor_agrim
    print ("")
    print ("===========================================")
    print ("Honorarios: $",honorarios)
    print (f"Sellados CPAM: ${sellado_cpam:.0f}")
    print ("===========================================")

replanteo_y_amojonamiento(nro_parcelas)