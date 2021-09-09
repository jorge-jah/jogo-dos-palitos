player1 = input("Digite o nome do Jogador 1: ")
player2 = input('Agora digite o nome do Jogador 2: ')
print('Ok', player1.title(),' e', player2.title(),' vamos iniciar.')
print()
print("Vamos jogar o jogo dos palitos.")
print()
print('JOGADOR 1')
n1 = input('Coloque a quantidade de palitos. De 0 a 3: ')
if n1 .isnumeric():
  n1 = int(n1)
  if n1 < 0:
    print('Quantidade não é válida.')
  elif n1 > 3:
    print('Quantidade não é válida.')
  else:
    print('Ok. gravei seu número.') 
else:
  print('Digite um número válido.')
print("\x1b[2J")

print('JOGADOR 2')
n2 = input('Coloque a quantidade de palitos. De 0 a 3: ')
if n2 .isnumeric():
  n2 = int(n2)
  if n2 < 0:
    print('Quantidade não é válida.')
  elif n2 > 3:
    print('Quantidade não é válida.')
  else:
    print('Ok. gravei seu número.') 
else:
  print('Digite um número válido.')
print("\x1b[2J")

print('Agora vamos aos palpites.')
print('Quantos palitos têm na rodada.')

print(player1.title())
palpite_1 = input('Digite seu palpite: ')
if palpite_1 .isnumeric():
  palpite_1 = int(palpite_1)
  if palpite_1 < 0:
    print('Quantidade não é válida.')
  elif palpite_1 > 6:
    print('Quantidade não é válida.')
  else:
    print('Ok. gravei seu número.') 
else:
  print('Digite um número válido.')

print(player2.title())
palpite_2 = input('Digite seu palpite: ')
if palpite_2 .isnumeric():
  palpite_2 = int(palpite_2)
  if palpite_1 < 0:
    print('Quantidade não é válida.')
  elif palpite_1 > 6:
    print('Quantidade não é válida.')
  else:
    print('Ok. gravei seu número.') 
else:
  print('Digite um número válido.')

print(player1.title(), 'você colocou', n1, 'palitos.')
print(player2.title(), 'você colocou', n2, 'palitos.')

resultado = n1 + n2
print('O total de palitos na rodada é: ', resultado)

if palpite_1 == resultado :
  print(player1.title(), 'venceu')
elif palpite_2 == resultado:
  print(player2.title(), 'venceu.')
else:
  print("Ninguém venceu essa rodada.")
