from colorama import Fore, Style

NARANJA = '\033[38;5;214m'
MAGENTA = '\033[38;5;201m'

def formato_moneda(valor):
    temp = f"{valor:,.2f}"
    return temp.replace(',', 'X').replace('.', ',').replace('X', '.')

def sellado_agrim_cpam(honorarios, v_matricula, v_auto, v_geo, v_agrim):
    """Fórmula auxiliar utilizada en todas las opciones para calcular el sellado."""
    matricula_honorarios = float(honorarios * (v_matricula / 100))
    matricula_geofada = round((matricula_honorarios + v_auto + v_geo) / v_agrim, 0)
    retenciones_cpam = matricula_geofada * v_agrim
    v_mat_cpam = v_matricula
    return retenciones_cpam, matricula_honorarios, v_mat_cpam, matricula_geofada


# =====================================================================
# OPCIONES DEL MENÚ (Lectura Lineal: Cálculos + Impresión)
# =====================================================================

def calcular_opcion_1_y_2(nro_parcelas, recargo, config):
    # 1. CÁLCULOS
    v_base = float(config['v_acta_base'])
    v_exc = float(config['v_acta_parcela'])
    n_parc = int(nro_parcelas)
    v_ajuste = float(config['v_ajuste_cpam'])
    
    honorarios_sin_ajuste = (v_base + (n_parc - 1) * v_exc)
    honorarios = honorarios_sin_ajuste * ((v_ajuste / 100) + 1)
    honorarios_extra = honorarios * (1 + (float(recargo) / 100))
    
    sellado_cpam, _, _, _ = sellado_agrim_cpam(
        honorarios, config['v_matricula'], config['v_autoconsulta'], config['v_geofada'], config['v_agrim']
    )
    
    res = honorarios_extra if recargo != 0 else honorarios

    # 2. IMPRESIÓN SIMPLE
    print("\n" + "-"*30)
    print(f"Honorarios: {NARANJA}${formato_moneda(res)}{Style.RESET_ALL}")
    print(f"Sellado CPAM: {NARANJA}${formato_moneda(sellado_cpam)}{Style.RESET_ALL}")
    print("-"*30 + "\n")


def calcular_opcion_4(nro_parcelas, recargo, config):
    
    v_base = float(config['v_mensura_base'])
    v_exc = float(config['v_mensura_parcela'])
    n_parc = int(nro_parcelas)
    va = float(config['v_ajuste_cpam'])
    
    honorarios_sin_ajuste = (v_base + (n_parc - 1) * v_exc)
    honorarios = honorarios_sin_ajuste * ((va / 100) + 1)
    honorarios_extra = honorarios * (1 + (float(recargo) / 100))
    
    sel, mh, vm, vgf = sellado_agrim_cpam(
        honorarios, config['v_matricula'], config['v_autoconsulta'], config['v_geofada'], config['v_agrim']
    )
    
    res = honorarios_extra if recargo != 0 else honorarios

    # 2. IMPRESIÓN DETALLADA
    print("\nPROCEDIMIENTO DE CÁLCULO DETALLADO")
    print("-"*70)
    print(f"1. Honorarios base + parcelas: {NARANJA}${formato_moneda(honorarios_sin_ajuste)}{Style.RESET_ALL}")
    print(f"2. Honorarios con {Fore.BLUE}{va}%{Style.RESET_ALL} de ajuste según CPAM: {NARANJA}${formato_moneda(honorarios)}{Style.RESET_ALL}")
    print(f"3. Honorarios con {Fore.BLUE}{recargo}%{Style.RESET_ALL} de recargo: {NARANJA}${formato_moneda(honorarios_extra)}{Style.RESET_ALL}")
    print("-"*70)
    print(f"4. {Fore.BLUE}{vm}%{Style.RESET_ALL} aplicado a honorarios del pto. 2: {NARANJA}${formato_moneda(mh)}{Style.RESET_ALL}")
    print(f"5. Cantidad de AGRIM redondeada: {NARANJA}{vgf:.0f}{Style.RESET_ALL}")
    print("-"*70)
    print(f"6. Sellado CPAM: {NARANJA}${formato_moneda(sel)}{Style.RESET_ALL}")
    print("-"*70)


def mensura_con_fraccionamiento(nro_parcelas, nro_edificadas, recargo, config):
    # 1. CÁLCULOS DE ESCALAS
    if nro_parcelas <= 5:
        base = config['v_frac_2_5_base']
        excedente_valor = config['v_frac_2_5_parc']
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

    honorarios_sin_ajuste = float(base + (cantidad_excedente * excedente_valor))
    incremento_edificado = nro_edificadas * config['v_frac_incremento_edificado']
    
    va = config['v_ajuste_cpam']
    honorarios = (honorarios_sin_ajuste + incremento_edificado) * ((va / 100) + 1)
    honorarios_extra = honorarios * (1 + (recargo / 100))

    sel, mh, vm, vgf = sellado_agrim_cpam(
        honorarios, config['v_matricula'], config['v_autoconsulta'], config['v_geofada'], config['v_agrim']
    )
    
    res = honorarios_extra if recargo != 0 else honorarios

    # 2. IMPRESIÓN DETALLADA
    print("\nPROCEDIMIENTO DE CÁLCULO DETALLADO")
    print("-"*70)
    print(f"1. Honorarios base + parcelas: {NARANJA}${formato_moneda(honorarios_sin_ajuste)}{Style.RESET_ALL}")
    print(f"2. Honorarios con {Fore.BLUE}{va}%{Style.RESET_ALL} de ajuste según CPAM: {NARANJA}${formato_moneda(res)}{Style.RESET_ALL}")
    print(f"3. Honorarios con {Fore.BLUE}{recargo}%{Style.RESET_ALL} de recargo: {NARANJA}${formato_moneda(honorarios_extra)}{Style.RESET_ALL}")
    print("-"*70)
    print(f"4. {Fore.BLUE}{vm}%{Style.RESET_ALL} aplicado a honorarios del pto. 2: {NARANJA}${formato_moneda(mh)}{Style.RESET_ALL}")
    print(f"5. Cantidad de AGRIM redondeada: {NARANJA}{vgf:.0f}{Style.RESET_ALL}")
    print("-"*70)
    print(f"6. Sellado CPAM: {NARANJA}${formato_moneda(sel)}{Style.RESET_ALL}")
    print("-"*70)