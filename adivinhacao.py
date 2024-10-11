print ('**********************************')
print ('*BEM VINDO AO JOGO DA ADIVINHACAO*')
print ('**********************************')
from random import randint
n = randint(1,5)
ne = int(input('escolha um numero: '))
if n == ne:
    print (f'voce ganhou! parabens! o numero era{n}')
else: 
    print (f'que pena! voce perdeu! o numero era {n}')