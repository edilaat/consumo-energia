nome=input("Qual o nome do aparelho? ")
potencia=input("Qual a potência do aparelho em watts? ")
tempo=input("Quantas horas por dia o aparelho fica ligado? ")

consumoMensal=float(potencia)*float(tempo)*30/1000
print("Aparelho:", nome)
print("Consumo estimado:",consumoMensal,"kWh/mês")
