          # Функция запроса натурального числа
def input_natural_number(Text):
    while True :
        try :
            N = int(input(Text))
            if N > 0 :
                return N
            else :
                print('Введено ненатуральное число.')
        except :
            print('Число не введено.')


          # Функция 