'''

BAR = 2x

BAR BAR = 4x

BAR BAR BAR = 6x

BOOST = 10x

777 = 50x

'''

import random
import os
import time


class Slot():
  def __init__(self, nome, multiplicador):
    self.nome = nome
    self.multiplicador = multiplicador


def economia(VALOR_JOGADA, DINHEIRO):
  on_screen = [BAR.nome, BAR_BAR.nome, BAR_BAR_BAR.nome, BOOST.nome, TRIPLE_SEVEN.nome]
  clear()
  while True:
    aleatorio = random.choices(on_screen, k=3)
    if DINHEIRO >= VALOR_JOGADA:
        print(f'SE VOCÊ QUISER VOLTAR PARA O MENU PRINCIPAL, DIGITE "SAIR" PARA SAIR OU "APOSTA" PARA MUDAR O VALOR DA APOSTA\n\nAPOSTA ATUAL: ${VALOR_JOGADA}\nDINHEIRO ATUAL: ${DINHEIRO}')
        op = lerstr('PRESSIONE QUALQUER TECLA PARA JOGAR\n: ')
        
        if op == 'SAIR':
            main()
            break
        if op == 'APOSTA':
            clear()
            jogada(DINHEIRO)
            break
        
        DINHEIRO -= VALOR_JOGADA

        clear()

        print('=-'*35)
        print(f'\n\t{aleatorio[0]}  ----------  {aleatorio[1]}  ----------  {aleatorio[2]}\n'.center(41))
        print('=-'*35)

        if aleatorio[0] == aleatorio[1] == aleatorio[2]:
            if aleatorio[0] == 'BAR':
                GANHOS = VALOR_JOGADA * BAR.multiplicador
                DINHEIRO += GANHOS
                MULTIPLICADOR = BAR.multiplicador

            if aleatorio[0] == 'BAR BAR':
                GANHOS = VALOR_JOGADA * BAR_BAR.multiplicador
                DINHEIRO += GANHOS
                MULTIPLICADOR = BAR_BAR.multiplicador

            if aleatorio[0] == 'BAR BAR BAR':
                GANHOS = VALOR_JOGADA * BAR_BAR_BAR.multiplicador
                DINHEIRO += GANHOS
                MULTIPLICADOR = BAR_BAR_BAR.multiplicador

            if aleatorio[0] == 'BOOST':
                GANHOS = VALOR_JOGADA * BOOST.multiplicador
                DINHEIRO += GANHOS
                MULTIPLICADOR = BOOST.multiplicador

            if aleatorio[0] == '777':
                GANHOS = VALOR_JOGADA * TRIPLE_SEVEN.multiplicador
                DINHEIRO += GANHOS
                MULTIPLICADOR = TRIPLE_SEVEN.multiplicador

            print(f'PARABÉNS! VOCÊ GANHOU UM MULTIPLICADOR DE {MULTIPLICADOR}x, APOSTANDO ${VALOR_JOGADA} DA UM GANHO DE: ${GANHOS}\nDINHEIRO ANTES DO GANHO: ${DINHEIRO-GANHOS}\nDINHEIRO DEPOIS DO GANHO: ${DINHEIRO}')
        
        if DINHEIRO <= 0:
            print('SALDO INSUFICIENTE\nREDIRECIONANDO PARA MENU PRINCIPAL...')
            time.sleep(3)
            main()
            break
    
    else:
        clear()
        print(f'SUA APOSTA É MAIOR QUE SEU DINHEIRO ATUAL, DIMINUA O VALOR DA APOSTA')
        jogada(DINHEIRO)
        break
  


def jogada(DINHEIRO):
  while True:
    if DINHEIRO >= 1:
        VALOR_JOGADA = lerint2(f'SEU DINHEIRO ATUAL: ${DINHEIRO}\nDIGITE O VALOR QUE VOCÊ QUER APOSTAR: $')
        if VALOR_JOGADA <= DINHEIRO and VALOR_JOGADA >= 1:
            economia(VALOR_JOGADA, DINHEIRO)
            break
        else:
            clear() 
            print(f'SUA APOSTA TEM QUE SER MENOR OU IGUAL QUE SEU DINHEIRO ATUAL E A APOSTA MINIMA É $1, SEU DINHEIRO ATUAL É ${DINHEIRO}')
            continue
    else:
       print('O DINHEIRO MINIMO TEM QUE SER $1')
       break
    


def lerstr(msg):
  while True:
    try:
      string = str(input(msg).strip().upper())
    except:
      clear()
    else:
      return string


def lerint(msg):
  while True:
    try:
      inteiro = int(input(msg).strip())
    except:
      clear()
      print('-'*40)
      print('BEM VINDO AO SLOT'.center(40))
      print('-'*40)
    else:
      return inteiro


def lerint2(msg):
  while True:
    try:
      inteiro = int(input(msg).strip())
    except:
      clear()
    else:
      return inteiro


def clear():
  if os.system == 'nt':
    os.system('cls')
  else:
    os.system('clear')


def main():
  global BAR, BAR_BAR, BAR_BAR_BAR, BOOST, TRIPLE_SEVEN

  BAR = Slot('BAR', 2)
  BAR_BAR = Slot('BAR BAR', 4)
  BAR_BAR_BAR = Slot('BAR BAR BAR', 6)
  BOOST = Slot('BOOST', 10)
  TRIPLE_SEVEN = Slot('777', 50)

  clear()

  while True:
    clear()
    print('-'*40)
    print('BEM VINDO AO SLOT'.center(40))
    print('-'*40)
    op = lerint('[ 1 ]NOVO JOGO\n[ 0 ]SAIR\nSUA ESCOLHA: ')
    if op == 0:
      clear()
      print('OBRIGADO POR JOGAR :)')
      break
    elif op == 1:
      clear()
      DINHEIRO = lerint2('QUANTO VOCÊ QUER DEPOSITAR? $')
      jogada(DINHEIRO)
      break
    else:
      continue

if __name__ == '__main__':
    main()