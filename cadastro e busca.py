print ('quer cadastrar alguem?')
print ('[0] sim')
print ('[1] nao')
c = input('escolha: ')
informacoes = list()
if c.isnumeric():
    c1 = int(c)
    while c1 == 0:
        e = input('email: ')
        n = input('nome: ')
        i = input('idade: ')
        dados= e, n, i
        informacoes.append(dados)
        print (dados)
        print ('quer cadastrar mais alguem?')
        print ('[0] sim')
        print ('[1] nao')
        c2 = input('escolha: ')
        if c2.isnumeric():
            c3 = int(c2)
            if c3 == 1:
                print(informacoes)
                print('encontrar alguem?')
                print ('[0] sim')
                print ('[1] nao')
                c4= input('escolha: ')
                if c4.isnumeric():
                    c5 = int(c4)
                    if c5 == 0:
                        c6 = input('nome da pessoa: ')
                        a=0
                        achei = False
                        while  a < len(informacoes) and achei==False:
                            if c6 == informacoes[a][1]:
                                
                                print (f'achei! O nome {c6} esta na posicao {a+1}')
                                print(informacoes[a])
                                achei = True
                            a+=1
                        if achei == False:
                            print (f'nao achei {c6}')            
                    elif c5 ==1:
                        break
            if c3 == 0: 
                continue
else:
    print ('voce escolheu nada')
