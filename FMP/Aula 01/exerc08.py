# salario + 15% - 8%

salario = float(input('Digite seu salário: '))
aumento = (salario * 0.15) + salario
desconto = (aumento * 8/100)
total = (aumento - desconto)
print('Seu salário inicial é de: R${}'.format(salario))
print('Após o aumento, seu sálario é: R${}'.format(aumento))
print('Com o desconto de impostos, seu salário ficará: R${}'.format(total))
