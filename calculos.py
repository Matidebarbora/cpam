def sellado_agrim_cpam(honorarios, v_matricula, v_auto, v_geo, v_agrim):
    retenciones_cpam = (round(((honorarios * (v_matricula / 100) + v_auto + v_geo) / v_agrim), 0)) * v_agrim
    return retenciones_cpam


def base_mas_excedente_parcela(valor_base, valor_excedente, nro_parcelas, recargo, config, valor_ajuste_cpam):
    
    v_base = float(valor_base)
    v_exc = float(valor_excedente)
    n_parc = int(nro_parcelas)
    v_ajuste = float(valor_ajuste_cpam)
    
    # Tu fórmula corregida
    honorarios = (v_base + (n_parc - 1) * v_exc) * ((v_ajuste / 100) + 1)
    
    honorarios_extra = honorarios * (1 + (float(recargo) / 100))
    
    sellado_cpam = sellado_agrim_cpam(
        honorarios, 
        config['v_matricula'], 
        config['v_autoconsulta'], 
        config['v_geofada'], 
        config['v_agrim']
    )
    
    return honorarios, honorarios_extra, sellado_cpam


def mensura_con_fraccionamiento(nro_parcelas, nro_edificadas, recargo, config):
    # 1. Determinación de tramos (Lógica de escalas)
    if nro_parcelas <= 5:
        base = config['v_frac_2_5_base']
        excedente_valor = config['v_frac_2_5_parc']
        # Si la base 2-5 ya incluye la primera parcela, aquí podrías necesitar nro_parcelas - 1
        # Pero usualmente en fraccionamiento la base cubre el "hasta 5"
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
    else:
        base = config['v_frac_mas120_base']
        excedente_valor = config['v_frac_mas120_parc']
        cantidad_excedente = nro_parcelas - 120

    # 2. Cálculo de Honorarios Base + Edificadas
    honorarios_sin_ajuste = float(base + (cantidad_excedente * excedente_valor))
    incremento_edificado = nro_edificadas * config['v_frac_incremento_edificado']
    
    # 3. Aplicación del Ajuste CPAM (6%)
    # Aplicamos el aumento del 6% a todo el honorario profesional
    valor_ajuste = config['v_ajuste_cpam']
    honorarios = (honorarios_sin_ajuste + incremento_edificado) * ((valor_ajuste / 100) + 1)

    # 4. Cálculo de Honorarios con Recargo (para el cliente)
    honorarios_extra = honorarios * (1 + (recargo / 100))

    # 5. Cálculo del Sellado (Sobre el honorario ajustado, pero sin el recargo)
    sellado_cpam = sellado_agrim_cpam(
        honorarios, 
        config['v_matricula'], 
        config['v_autoconsulta'], 
        config['v_geofada'], 
        config['v_agrim']
    )

    return honorarios, honorarios_extra, sellado_cpam