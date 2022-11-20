nome1 = input()
nome2 = input()
nome3 = input()

#quando algum for divisivel por 10
if len(nome1) % 10 == 0 or len(nome2) % 10 == 0 or len(nome3) % 10 == 0:
    print(f'Divisivelpordez')


#quando todos forem divisiveis
elif len(nome1) % 2 == 0 and len(nome2) % 10 == 0 and len(nome3):
    print(nome1+nome2+nome3)


#divisivel apenas por 2 
elif len(nome1) % 2 == 0 and len(nome2) % 3 != 0 and len(nome3) % 5 != 0:
    print(nome1)
#divisivel apenas por 3
elif len(nome1) % 2 != 0 and len(nome2) % 3 == 0 and len(nome3) % 5 != 0:
    print(nome2)
#divisivel apenas por 5
elif len(nome1) % 2 != 0 and len(nome2) % 3 != 0 and len(nome3) % 5 == 0:
    print(nome3)


#quando nome 1 e 2 forem divisiveis e nome 3 não
elif len(nome1) % 2 == 0 and len(nome2) % 3 == 0 and len(nome3) % 5 !=0:
    print(nome1+nome2)
#quando nome1 nao é divisivel mas nome 2 e 3 é divisivel
elif len(nome1) % 2 != 0 and len(nome2) % 3 == 0 and len(nome3) % 5 ==0:
    print(nome2+nome3)
#quando nome 1 e 3 são divisiveis e nome 2 não
elif len(nome1) % 2 == 0 and len(nome2) % 3 != 0 and len(nome3) % 5 == 0:
    print(nome1+nome3)

#caso nenhuma opção acima seja verdadeira
else:
    print(f'Não tem nome')
