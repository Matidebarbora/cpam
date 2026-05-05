from variables import valor_autoconsulta, valor_geofada, valor_agrim, valor_matricula

def sellado_agrim_cpam (honorarios):
    # Devuelve el cálculo de sellado CPAM considerando los Agrim redondeados
    retenciones_cpam = (round(((honorarios * (valor_matricula / 100) + valor_autoconsulta + valor_geofada) / valor_agrim), 0)) * valor_agrim
    return retenciones_cpam


def base_mas_excedente_parcela (valor_base, valor_excedente, nro_parcelas, recargo):
    honorarios = float(valor_base + nro_parcelas * valor_excedente)
    honorarios_extra = honorarios * (1 + (recargo / 100))
    sellado_cpam = sellado_agrim_cpam (honorarios)

    return honorarios, honorarios_extra, sellado_cpam
