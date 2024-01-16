"""Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
___________________
"""

# Código para “todos os números exceto o #13”:

andarNo = 1

while andarNo <=20:
  if andarNo == 13:
    andarNo = andarNo + 1
    continue
  else:
    print(andarNo)
  andarNo = andarNo + 1


# Código para imprimir todos os andares de forma decrescente, exceto #13:

andarNo = 20

while andarNo >=1:
  if andarNo == 13:
    andarNo = andarNo - 1
    continue
  else:
    print(andarNo)
  andarNo = andarNo - 1
