# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

num = int(input('Informe qual tabuada dezeja visualizar: '))

for i in range(1, 10):
    print(num, 'x', i, '=', num*i)
