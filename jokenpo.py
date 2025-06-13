print ('*********')
print ('*JOKENPO*')
print ('*********')
while True:
    print ('-----------')
    print ('menu:')
    print ('[0] pedra')
    print ('[1] papel')
    print ('[2] tesoura')
    print ('-----------')
    from random import randint
    c = randint(0,2)
    p = int(input ('escolha:'))
    if p <0 or p >2:
        print ('escolha errada, man')
    elif c==0 and p==2:
        print ('voce perdeu! Escolhi pedra')
    elif c==1 and p==0:
        print ('voce perdeu! Escolhi papel')
    elif c==2 and p==1:
        print ('voce perdeu! Escolhi tesoura')
    elif c==p:
        print ('empate!')
    else:
        print ('voce ganhou')
print ('acabou!')