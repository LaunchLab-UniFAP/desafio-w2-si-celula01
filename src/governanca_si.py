# LaunchLab UniFAP - Desenvolvimento Exclusivo SI
METADADOS_COMPLIANCE = {
    "limite_frota_m3": 50.0,
    "piso_ociosidade_percentual": 0.30, 
    "indicadores_ambientais": ["Reducao CO2", "Economia Combustivel"]
}

def calcular_eficiencia_financeira(volume_final):
    piso_critico = METADADOS_COMPLIANCE["limite_frota_m3"] * METADADOS_COMPLIANCE["piso_ociosidade_percentual"]
    
    if volume_final < piso_critico:
        return "Alerta: Alto Custo de Ociosidade Detectado"
    return "Eficiencia Economica Aceitavel"

if __name__ == "__main__":
    print(calcular_eficiencia_financeira(12.5)) 
