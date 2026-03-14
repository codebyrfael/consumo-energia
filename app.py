print("⚡ Calculadora de Consumo de Energia ⚡")

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

# Cálculo do consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo estimado
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

# Resultado
print("\n📊 Resultado")
print("Aparelho:", aparelho)
print("Consumo estimado:", round(consumo_mensal, 2), "kWh/mês")
print("Custo estimado: R$", round(custo_estimado, 2))
