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
        print(f'IF YOU WANT GO BACK TO THE MAIN MENU, TYPE "EXIT" OR "BET" TO CHANGE THE BET VALUE\n\nCURRENT BET: ${VALOR_JOGADA}\nCURRENT CASH: ${DINHEIRO}')
        op = lerstr('PRESS ANY KEY TO PLAY\n: ')
        
        if op == 'EXIT':
            main()
            break
        if op == 'BET':
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

            print(f'CONGRATS! YOU WIN A MULTIPLIER OF {MULTIPLICADOR}x, BETTING ${VALOR_JOGADA} GIVES YOU A GAIN OF: ${GANHOS}\nMONEY BEFORE THE GAINS: ${DINHEIRO-GANHOS}\nMONEY AFTER THE GAINS: ${DINHEIRO}')
        
        if DINHEIRO <= 0:
            print('YOUR MONEY IS OVER.\nREDIRECTING TO MAIN MENU...')
            time.sleep(3)
            main()
            break
    
    else:
        clear()
        print(f'YOUR BET IS HIGHER THAN YOUR CURRENT MONEY, PLACE A LOWER BET')
        jogada(DINHEIRO)
        break
  


def jogada(DINHEIRO):
  while True:
    if DINHEIRO >= 1:
        VALOR_JOGADA = lerint2(f'YOUR CURRENT CASH: ${DINHEIRO}\nTYPE THE VALUE YOU WANT TO BET: $')
        if VALOR_JOGADA <= DINHEIRO and VALOR_JOGADA >= 1:
            economia(VALOR_JOGADA, DINHEIRO)
            break
        else:
            clear()
            print(f'YOUR BET HAS TO BE LOWER THAN YOUR CURRENT CASH AND THE MINIMUM BET IS $1, YOU CURRENT CASH IS ${DINHEIRO}')
            continue
    else:
       print('YOUR MINIMUM CASH HAS TO BE $1')
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
      print('WELCOME TO SLOT'.center(40))
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
    os.system('clear')
  else:
    os.system('cls')


def main():
  global BAR, BAR_BAR, BAR_BAR_BAR, BOOST, TRIPLE_SEVEN

  BAR = Slot('BAR', 2)
  BAR_BAR = Slot('BAR BAR', 4)
  BAR_BAR_BAR = Slot('BAR BAR BAR', 6)
  BOOST = Slot('BOOST', 10)
  TRIPLE_SEVEN = Slot('777', 50)

  while True:
    clear()
    print('-'*40)
    print('WELCOME TO SLOT'.center(40))
    print('-'*40)
    op = lerint('[ 1 ]NEW GAME\n[ 0 ]EXIT\nYOUR CHOICE: ')
    if op == 0:
      clear()
      print('THANK YOU FOR PLAYING :)')
      break
    elif op == 1:
      clear()
      DINHEIRO = lerint2('HOW MUCH DO YOU WANT TO DEPOSIT? $')
      jogada(DINHEIRO)
      break
    else:
      continue

if __name__ == '__main__':
    main()