tempo = float(input("Digite o tempo de viagem (horas): "))
velocidade = float(input("Digite a velocidade média (km/h): "))

distancia = tempo * velocidade
litros = distancia / 12

print("Litros de combustível gastos:", litros)