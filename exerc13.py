salario = float(input(
    'Para saber quanto ficará seu salário após o aumento de 15%, digite seu salario: '))
salario_aumento = salario + (salario * 0.15)  # ou 15/100
print('Seu salário após o aumento é de: R${}'.format(salario_aumento))
