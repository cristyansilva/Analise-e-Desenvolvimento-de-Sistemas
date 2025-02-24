'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''
salario = float(input('Digite o sálario atual do funcionário: R$'))
if salario <= 280:
    perc = 20/100
    aumento = (salario * perc)
    salario_aumento = salario + aumento
    print(f'O salário ficará: \033[32mR${salario_aumento:.2f}\033[m')
    print(f'O Percentual de aumento é {perc}%')
    print(f'O valor do aumento aplicado foi: R${aumento}')

elif salario >= 280 and salario <= 700:
    perc = 15/100
    aumento = (salario * perc)
    salario_aumento = salario + aumento
    print(f'O salário ficará \033[32mR${salario_aumento:.2f}\033[m')
    print(f'O Percentual de aumento é {perc}%')
    print(f'O valor do aumento aplicado foi: R${aumento}')

elif salario >= 700 and salario <= 1500:
    perc = 10/100
    aumento = (salario * perc)
    salario_aumento = salario + aumento
    print(f'O salário ficará \033[32mR${salario_aumento:.2f}\033[m')
    print(f'O Percentual de aumento é {perc}%')
    print(f'O valor do aumento aplicado foi: R${aumento}')

elif salario > 1500:
    perc = 5/100
    aumento = (salario * perc)
    salario_aumento = salario + aumento
    print(f'O salário ficará \033[32mR${salario_aumento:.2f}\033[m')
    print(f'O Percentual de aumento é {perc:}%')
    print(f'O valor do aumento aplicado foi: R${aumento}')
print(f'O salário antes do Ajuste era R${salario:.2f}')
