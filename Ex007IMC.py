from time import sleep
print('-=-' * 5)
print('CALCULANDO IMC')
print('-=-' * 5)
peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print('--' * 10)
print('CALCULANDO!!!')
sleep(2)
if imc < 18.5:
    print('Você está abaixo do seu peso, IMC de {:.1f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está no seu peso ideal!, IMC de {:.1f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso! IMC de {:.1f}'.format(imc))
elif imc >= 30 and imc <40:
    print('Você esta obeso! IMC de {:.1f}'.format(imc))
else:
    print('Obesidade MÓRBIDA, IMC de {:.1f}'.format(imc))