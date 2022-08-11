num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter par HEXADECIMAL''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('O valor {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O valor {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O valor {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida. Tente novamente!')
