#interrrompe quando o jogador perde
total = ganhou =  0 
import random
while True:
    print('-=-'*10)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('-=-'*10)
    jogador = int(input('digite um valor:'))
    valor = str(input('Par ou Ìmpar?[P/I]'))
    if valor != 'p' or valor != 'i':
            valor = str(input('Par ou Impar[P/I]'))
    computador = random.randint(0,10)
    soma = jogador + computador
    if jogador % 2 == 0 and soma % 2 == 0:
        total = total+1
        print(f'voce jogou {jogador}e {computador}.A soma da {soma} que é PAR.jogador ganhou')

    if jogador % 2 > 0 and soma % 2 > 0:
        print(f'voce jogou {jogador}e o computador {computador} . A soma é {soma} que é IMPAR.jogador ganhou')
        total=total+1
    if jogador % 2 == 0 and soma % 2 > 0:
        
        print(f'voce jogou {jogador} e o computador {computador}. A soma é {soma} é IMPAR.jogador perdeu')
        
        break
    if jogador % 2 > 0 and soma % 2 == 0:
    
        print(f'voce jogou {jogador} e o computador {computador} A soma é {soma} que é PAR.jogador perdeu')
        
        break
print(f' voce ganhou {total} vezes...')
