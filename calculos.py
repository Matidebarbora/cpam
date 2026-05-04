from variables import valor_base_acta, valor_parcela, valor_autoconsulta, valor_geofada, valor_agrim, valor_matricula

def replanteo_y_amojonamiento (nro_parcelas, recargo):
    
    honorarios = float((valor_base_acta + valor_parcela) + ((nro_parcelas - 1) * valor_parcela))
    honorarios_extra = honorarios * (1 + (recargo / 100))
    retenciones_cpam = round(((honorarios * (valor_matricula / 100) + valor_autoconsulta + valor_geofada) / valor_agrim), 0)
    sellado_cpam = retenciones_cpam * valor_agrim

    return honorarios, honorarios_extra, sellado_cpam
