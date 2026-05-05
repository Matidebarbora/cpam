from variables import valor_base_acta, valor_parcela, valor_autoconsulta, valor_geofada, valor_agrim, valor_matricula, valor_parcela_mensura, valor_parcela_excedente_mensura

def sellado_agrim_cpam (honorarios):
    # Devuelve el cálculo de sellado CPAM considerando los Agrim redondeados
    retenciones_cpam = (round(((honorarios * (valor_matricula / 100) + valor_autoconsulta + valor_geofada) / valor_agrim), 0)) * valor_agrim
    return retenciones_cpam


def replanteo_y_amojonamiento (nro_parcelas, recargo):
    honorarios = float((valor_base_acta + valor_parcela) + ((nro_parcelas - 1) * valor_parcela))
    honorarios_extra = honorarios * (1 + (recargo / 100))
    sellado_cpam = sellado_agrim_cpam (honorarios)

    return honorarios, honorarios_extra, sellado_cpam

def mensura_simple_urbana (nro_parcelas, recargo):
    honorarios = float(valor_parcela_mensura + (nro_parcelas * valor_parcela_excedente_mensura))
    honorarios_extra = honorarios * (1 + (recargo / 100))
    sellado_cpam = sellado_agrim_cpam (honorarios)

    return honorarios, honorarios_extra, sellado_cpam