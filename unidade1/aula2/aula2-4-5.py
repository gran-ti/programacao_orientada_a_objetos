semana = int(input('digite um numero: '))
match semana:
    case 1:
        print('domingo')
    case 2:
        print ('segunda')
    case 3:
        print('terça')
    case 4:
        print ('quarta')
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sabado')
    case other:
        print('Dia invalido')