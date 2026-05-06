def sellado_agrim_cpam(honorarios, v_matricula, v_auto, v_geo, v_agrim):
    retenciones_cpam = (round(((honorarios * (v_matricula / 100) + v_auto + v_geo) / v_agrim), 0)) * v_agrim
    return retenciones_cpam


def base_mas_excedente_parcela(valor_base, valor_excedente, nro_parcelas, recargo, config):
    honorarios = float(valor_base + nro_parcelas * valor_excedente)
    honorarios_extra = honorarios * (1 + (recargo / 100))
    sellado_cpam = sellado_agrim_cpam(
        honorarios, 
        config['valor_matricula'], 
        config['valor_autoconsulta'], 
        config['valor_geofada'], 
        config['valor_agrim']
    )

    return honorarios, honorarios_extra, sellado_cpam