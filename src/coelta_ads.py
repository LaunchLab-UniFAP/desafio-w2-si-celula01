# LaunchLab UniFAP - Desenvolvimento Exclusivo ADS
def processar_motor_coleta():
    limite_maximo = 50.0
    volume_acumulado = 0.0
    
    print("--- MOTOR OPERACIONAL DE COLETA (ADS) ---")
    
    while True:
        try:
            entrada = input("Digite o volume da cacamba (m³) ou -1 para encerrar: ")
            volume = float(entrada)
            
            if volume == -1:
                break
                
            if volume < 0:
                print("Erro: Entrada Invalida")
                continue
                
            volume_acumulado += volume
            
            if volume_acumulado >= limite_maximo:
                print("Status: Capacidade Maxima Atingida")
                break
        except ValueError:
            print("Erro: Entrada Invalida")
            
    print(f"Volume Total: {volume_acumulado} m³")

if __name__ == "__main__":
    processar_motor_coleta()
