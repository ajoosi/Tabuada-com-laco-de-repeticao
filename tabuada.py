#while True --Looping infinito
# For c in range --Laço de repetição
# if n < 0: --- Se o numero digitado for menor que zero (NEGATIVO) pare o programa.

while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0:
        break
    print('--'* 30)
    for c in range(1,11):
        print(f'{n} x {c}  = {n*c}')
    print('--'*30)
print('PROGRAMA TABUADA ENCERRADO.')
