horas = float(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor por hora: "))
desconto = float(input("Digite o percentual de desconto: "))
dependentes = int(input("Digite o número de dependentes: "))

salario_bruto = horas * valor_hora
valor_desconto = salario_bruto * (desconto / 100)

salario_liquido = salario_bruto - valor_desconto
salario_liquido = salario_liquido + (dependentes * 100)

print("Salário a receber:", salario_liquido)