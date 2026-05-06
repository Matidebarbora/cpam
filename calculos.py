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


def mensura_con_fraccionamiento(nro_parcelas, recargo, config):
    # Determinamos los valores base y excedentes según el tramo
    if nro_parcelas <= 5:
        base = config['v_frac_2_5_base']
        excedente_valor = config['v_frac_2_5_parc']
        # En el primer tramo (2 a 5), se cobra el excedente por cada parcela directamente
        cantidad_excedente = nro_parcelas 
    
    elif nro_parcelas <= 20:
        base = config['v_frac_6_20_base']
        excedente_valor = config['v_frac_6_20_parc']
        cantidad_excedente = nro_parcelas - 5
        
    elif nro_parcelas <= 50:
        base = config['v_frac_21_50_base']
        excedente_valor = config['v_frac_21_50_parc']
        cantidad_excedente = nro_parcelas - 20
        
    elif nro_parcelas <= 120:
        base = config['v_frac_51_120_base']
        excedente_valor = config['v_frac_51_120_parc']
        cantidad_excedente = nro_parcelas - 50
        
    else: # Más de 120
        base = config['v_frac_mas120_base']
        excedente_valor = config['v_frac_mas120_parc']
        cantidad_excedente = nro_parcelas - 120

    # Cálculo de honorarios
    honorarios = float(base + (cantidad_excedente * excedente_valor))
    honorarios_extra = honorarios * (1 + (recargo / 100))
    
    # Cálculo del sellado (reutilizamos tu función existente)
    sellado_cpam = sellado_agrim_cpam(
        honorarios, 
        config['v_matricula'], 
        config['v_autoconsulta'], 
        config['v_geofada'], 
        config['v_agrim']
    )

    return honorarios, honorarios_extra, sellado_cpam