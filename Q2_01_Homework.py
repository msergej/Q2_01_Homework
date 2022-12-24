import os
os.system('cls||clear')
          # Для sympy работает только на уровне модуля, я не отдельной def()
import pandas as pd
import sympy
from sympy import *
import requests
import string
import telebot
from bot_tg import Token
# import json

          # Домашнее задание к уроку 10
# Задание: cоздать бота для вывода текущего курса валют(желательно запрос по конкретной валюте)
# /currency USD
def cbr_exchange_rate(currency):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    courses_table = pd.DataFrame(res['Valute']).T
    courses_table["Изменение (%)"] = courses_table.apply(lambda row: round((row.Value/row.Previous-1)*100,2) if row.Value/row.Previous >=1 else round(-(1- row.Value/row.Previous)*100,2), axis = 1)
    courses_table.rename(columns={'Nominal': 'Единиц', 'Name': 'Валюта', 'Value': 'Курс', 'Previous': 'Предыдущий курс'}, inplace=True)
    courses_table.drop(["ID", "NumCode", "CharCode"], axis=1, inplace=True)
    
    if str.upper(currency) in courses_table.index :
        currency_list = []
        currency_list.append(str.upper(currency))
        return courses_table[courses_table.index.isin(currency_list)]
    elif str.lower(currency) == 'all' : return courses_table
    else : return courses_table[courses_table.index.isin([])]

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    match message.text:
        case '/help': bot.reply_to(message, "Для получения курса валюты введите команду '/cur XXX', где XXX - код валюты. Для получения курсов всех валют наберите '/cur ALL'.")
        case '/start': bot.reply_to(message, "Вводите команду.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    currency = str(message.text)[5:]
    if not cbr_exchange_rate(currency).empty : bot.send_message(message.chat.id, cbr_exchange_rate(currency).to_string())
    else : bot.send_message(message.chat.id, "Введен неверный код валюты!")  

print("Бот запущен.")
bot.infinity_polling()


'''
          # Домашнее задание к уроку 06
# Задача: предложить улучшения кода для уже решённых задач.
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension и т.п. 3 любых заданий (из любого урока).
def Task_06_01_Ex_02_03(n):
          # Задание 01 (урок 2). Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
    from functools import reduce

    List = [(1+1/i)**i for i in range(1, n+1)]
    print("Начальные (" + str(n) + ") элементы ряда: " + str(List))
    ListSum = reduce(lambda x, y: x + y, List)
    return "Сумма начальных (" + str(n) + ") элементов ряда равна " + str(ListSum) + ", среднее значение - " + str(ListSum / n) + "."
def Task_06_02_Ex_02_01(N):
          # Задание 01 (урок 2). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример: 6782 -> 23, 0,56 -> 11.
    from functools import reduce

    DigitsList = {'0','1','2','3','4','5','6','7','8','9'}     
    Nstr = str(N)
    Nlist = list(map((lambda x: int(x) if (x in DigitsList) else 0), Nstr))
    DigitsSum = reduce(lambda x, y: x + y, Nlist)
    return "Сумма цифр числа " + str(N) + " составляет: " + str(DigitsSum) + "."
def Task_06_03_Ex_03_01(N):
          # Задание 1 (урок 3). Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов, стоящих на нечётных позициях.
    import random
    from functools import reduce

    List = [random.randint(-100,101) for i in range(0, N)]
    print("Заданный список: ", List)
    OddPositionsList = list(List[i] if i%2 != 0 else 0 for i in range(len(List)))
    OddPositionsSum = reduce(lambda x, y: x + y, OddPositionsList)
    return "Сумма элементов, на нечетных позициях: " + str(OddPositionsSum) + "." 

          # Запуск задания 01                 
print(Task_06_01_Ex_02_03(10))
          # Запуск задания 02                 
print(Task_06_02_Ex_02_01(12345.6789))
          # Запуск задания 03
print(Task_06_03_Ex_03_01(6))
'''
'''
          # Домашнее задание к уроку 05
# Задание 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
def Task_05_01a_Сandies_HvsH(N, TurnMax):
    import OwnFunctions as OFs

    print("Всего в игре", N, "конфет. За каждый ход игрок может взять не более", TurnMax, "конфет.")
    print("Для ОСТАНОВКИ игры необходимо ввести число, большее чем", N, ".")
    Rounds = 0
    Wins = [0, 0] 
    TurnCandies = 0
    while (TurnCandies < N+1):
        Rounds += 1
        Player = Rounds % 2 + 1
        LeftCandies = N
        print("Раунд №", Rounds, "( начинает игрок", Player, ").")
        while LeftCandies > 0 :
            TurnCandies = Task_05_01c_СurrentTurn(Player, TurnMax, LeftCandies, N+1)
            if TurnCandies > N :        # Выход, если введено число, превышающее первоначальное количество.
                break
            LeftCandies -= TurnCandies
            if (LeftCandies == 0): 
                Wins[Player-1] += 1
                break
            if (Player == 1): Player = 2         # Смена игрока
            else: Player = 1 
        if TurnCandies > N :            # Выход из игры, если введено число, превышающее первоначальное количество.
            break
    return "Сыграно раундов: " + str(Rounds-1) + ", общий счет - " + str(Wins[0]) + ":" + str(Wins[1]) + ". Спасибо за игру!"
def Task_05_01b_Сandies_HvsB(N, TurnMax):
    import OwnFunctions as OFs

    print("Всего в игре", N, "конфет. За каждый ход можно взять не более", TurnMax, "конфет.")
    print("Для ОСТАНОВКИ игры необходимо ввести число, большее чем", N, ".")
    print("БОТ играет под номером 1 и не может остановить игру принудительно.")
    Rounds = 0
    Wins = [0, 0] 
    TurnCandies = 0
    while (TurnCandies < N+1):
        Rounds += 1
        Player = Rounds % 2 + 1
        LeftCandies = N
        print("Раунд №", Rounds, "( начинает игрок", Player, ").")
        while LeftCandies > 0 :
            if (Player == 2): TurnCandies = Task_05_01c_СurrentTurn(Player, TurnMax, LeftCandies, N+1)
            else:                       # Ход БОТ-а (оптимальное или минимальное число конфет)
                TurnCandies = LeftCandies % (TurnMax + 1)
                if (TurnCandies == 0): TurnCandies = 1
                print("БОТ: оставшихся конфет -", LeftCandies, ", беру", TurnCandies)
            if TurnCandies > N :        # Выход, если введено число, превышающее первоначальное количество.
                break
            LeftCandies -= TurnCandies
            if (LeftCandies == 0): 
                Wins[Player-1] += 1
                break
            if (Player == 1): Player = 2         # Смена игрока
            else: Player = 1 
        if TurnCandies > N :            # Выход из игры, если введено число, превышающее первоначальное количество.
            break
    return "Сыграно раундов: " + str(Rounds-1) + ", общий счет - " + str(Wins[0]) + ":" + str(Wins[1]) + ". Спасибо за игру!"
def Task_05_01c_СurrentTurn(Player, TurnMax, Left, Exit):
    import OwnFunctions as OFs
          # Повторный ввод запрашивается, если ход больше оставшегося числа или больше максимально возможного на взятие. 
    TurnCandies = OFs.input_natural_number("Игрок " + str(Player) + ", введите число желаемых конфет из " + str(Left) + ": ")
    while (TurnCandies < Exit) and ((TurnCandies > TurnMax) or (TurnCandies > Left)):
        if (TurnCandies > Left) :
            print("В игре осталось только", Left, "конфет!")
            TurnCandies = OFs.input_natural_number("Игрок " + str(Player) + ", введите число желаемых конфет из " + str(Left) + ": ")
        else:
            print("Вы не можете взять более", TurnMax, "конфет!")
            TurnCandies = OFs.input_natural_number("Игрок " + str(Player) + ", введите число желаемых конфет из " + str(Left) + ": ")
    return TurnCandies
# Задание 2. Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)
def Task_05_02_X_0(N):
    import OwnFunctions as OFs

    print("Для ОСТАНОВКИ игры необходимо ввести целое число больше 9.")
    Rounds = 0
    Score = [0, 0, 0] 
    Field = []
    Field = [x+1 for x in range(9)]
    print("Нумерация ячеек игрового поля:")
    Task_05_02_X_0_FieldPrint(Field)
    Field = [Field[i]*0 for i in range(9)]
          # Исходное поле заполняется нулями, 1-й игрок ставит единицы, 2-й - двойки.
    print("Текущее состояние игрового поля:")
    Task_05_02_X_0_FieldPrint(Field)
    TurnField = 0
    while (TurnField <= N):
        Rounds += 1
        Player = Rounds % 2 + 1
        LeftFields = N
        print("Раунд №", Rounds, "( начинает игрок", Player, ").")
        while LeftFields > 0 :
            TurnField = Task_05_02_СurrentTurn(Field, Player, 9+1)
            if TurnField > N :        # Выход, если введено число, превышающее N.
                break
            Field[TurnField-1] = Player
            print("Текущее состояние игрового поля:")
            Task_05_02_X_0_FieldPrint(Field)
                                      # Завершение раунда и очистка поля, если выявлен победитель.
            Winner =  Task_05_02_X_0_WinnerCheck(Field)
            if Winner > 0 :
                Score[Winner-1] += 1
                Field = [Field[i]*0 for i in range(9)]
                break
            LeftFields -= 1
            if (LeftFields == 0):     # Завершение раунда и очистка поля, если поле заполнено полностью (записывается ничья).
                Score[2] += 1
                Field = [Field[i]*0 for i in range(9)]
                break
            if (Player == 1): Player = 2         # Смена игрока
            else: Player = 1 
        if (TurnField > N): break       # Выход из игры, если введено число, превышающее N.
    return "Сыграно раундов: " + str(Rounds-1) + ", общий счет - " + str(Score[0]) + ":" + str(Score[1]) + "=" + str(Score[2]) + ". Спасибо за игру!"
def Task_05_02_X_0_FieldPrint(Field):
    for i in range(3):
        print(Field[i*3+0], " ",Field[i*3+1], " ", Field[i*3+2])
    return 0    
def Task_05_02_СurrentTurn(Field, Player, Exit):
    import OwnFunctions as OFs
          # Повторный ввод запрашивается, если имеет место попытка хода в заполненную ячейку. 
    TurnFieldNumber = OFs.input_natural_number("Игрок " + str(Player) + ", введите номер поля ")
    while (TurnFieldNumber < Exit) and (Field[TurnFieldNumber-1] !=0):
        print("Поле", TurnFieldNumber, "уже заполнено!")
        TurnFieldNumber = OFs.input_natural_number("Игрок " + str(Player) + ", введите номер поля:")
    return TurnFieldNumber
def Task_05_02_X_0_WinnerCheck(Field):
    if (Field[0] == Field[1] == Field[2]): return Field[0]
    elif (Field[3] == Field[4] == Field[5]): return Field[3]
    elif (Field[6] == Field[7] == Field[8]): return Field[6]
    elif (Field[0] == Field[3] == Field[6]): return Field[0]
    elif (Field[1] == Field[4] == Field[7]): return Field[1]
    elif (Field[2] == Field[5] == Field[8]): return Field[2]
    elif (Field[0] == Field[4] == Field[8]): return Field[0]
    elif (Field[2] == Field[4] == Field[6]): return Field[2]
    else: return 0    

          # Запуск задания 01 (Вместо 117 - первый задаваемый параметр)
# if (int(input("Для игры с БОТ-ом введите 1: ")) != 1): print(Task_05_01a_Сandies_HvsH(65,28))
# else: print(Task_05_01b_Сandies_HvsB(65,28))
          # Запуск задания 02                 
print(Task_05_02_X_0(9))
'''
'''
          # Домашнее задание к уроку 04
# Задание 1. Вычислить число Пи c заданной точностью d.
# *Пример:* при d = 0.001, π = 3.141; при d = 0.0001, π = 3.1415.
def Task_04_01_Shrinked_PI():
    from mpmath import mp

    D = int(input("Введите требуемое число знаков π после запятой (от 0 до 100):"))
    if D>=1 and D<=100 :
        mp.dps = 101
        return str(mp.pi)[:D+2]
    else :
        return "Некорректно указано число знаков после запятой (" + str(D) + ")."
# Задание 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [2,3]; * 144 -> [2,3].
def Task_04_02_UniqueSimpleDivisors():
    import OwnFunctions as OFs
    import pandas as pd

    N = OFs.input_natural_number("Введите натуральное число: ")
    Num = N
    SimpleDivisors = [1]
    Devisor = 2               # Разложение числа на простые делители
    while N > 1:
        if N % Devisor == 0:
            SimpleDivisors.append(Devisor)
            N = N / Devisor
        else:
            Devisor += 1
    return "Уникальные простые делители числа " + str(Num) + ": " + str(pd.Series(SimpleDivisors).drop_duplicates().tolist())
# Задание 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def Task_04_03_UniqueListElements(N):
    import random  
    import pandas as pd

    List = [random.randint(0,20) for i in range(0, N)]
    print("Исходная последовательность", N, "чисел:", List)
    return "Уникальные значения (" + str(len(pd.Series(List).drop_duplicates().tolist())) + ") в исходной последовательности:" +\
           str(pd.Series(List).drop_duplicates().tolist())
# Задание 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена,
# и записать в файл многочлен степени k.(записать в строку)
# Пример: k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2; k=3 => 2*x^3 + 4*x^2 + 4*x + 5
def Task_04_04_Polynomial():
    import OwnFunctions as OFs
    import random

    N = OFs.input_natural_number("Введите натуральное число - степень многочлена: ")        
    if (N <= 12) :
        Сoefficients = [random.randint(-100,100) for i in range(N+1)]
        print("Коэффициенты многочлена: ", Сoefficients)
        x = Symbol('x')
        TitleText = "Многочлен степени " + str(N) + " с заданными коэффициентами: \n"
        Polynomial = str(sum(map(prod,zip(Сoefficients,[x**i for i in range(N,-1,-1)]))))
        File = open("HW_task_04_04.txt", "w")
        File.write(TitleText)
        File.write(Polynomial)
        File.close()
        return TitleText + Polynomial
    else :
        return "Слишком высокая степень многочлена!"
# Задание 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt : 2*x**2 + 4*x + 5; в file2.txt: 4*x**2 + 1*x + 4; результирующий файл: 6*x**2 + 5*x + 9
def Task_04_05_PolynomialSum() :
    FileIn = open("HW_task_04_05_In_1.txt", "r")
    P_1 = FileIn.read()
    FileIn.close()
    FileIn = open("HW_task_04_05_In_2.txt", "r")
    P_2 = FileIn.read()
    FileIn.close()    
    print("Первый многочлен: ", P_1)
    print("Второй многочлен: ", P_2)
   
    x = Symbol('x')
    P_Mult = simplify(P_1) + simplify(P_2)
    print("Результат сложения многочленов: ",P_Mult)
    FileOut = open("HW_task_04_05_Out.txt", "w")
    FileOut.write(str(P_Mult))
    FileOut.close()
    return "Результат сложения многочленов записан в файл."

          # Запуск задания 01                 
print(Task_04_01_Shrinked_PI())
          # Запуск задания 02                 
print(Task_04_02_UniqueSimpleDivisors())
          # Запуск задания 03                 
print(Task_04_03_UniqueListElements(15))
          # Запуск задания 04                 
print(Task_04_04_Polynomial())
          # Запуск задания 05                 
print(Task_04_05_PolynomialSum())
'''
'''
          # Домашнее задание к уроку 03
# Задание 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.
# *Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def Task_1_OddPositionsSum():
    import random
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

    OddPositionsSum = 0
    N = input_natural_number("Введите натуральное число - длину списка:")
    List = [random.randint(-1000,1001) for i in range(0, N)]
    print("Список чисел:", List)
    for i in range (len(List)):
        if i%2 == 1 :
            OddPositionsSum += List[i]

    return OddPositionsSum
# Задание 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:* [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
def Task_2_PairsProducts(N):
    import random  
    import math 

    List = [random.randint(-10,11) for i in range(0, N)]
    print("Список чисел:", List)
    ProductsList = []
    for i in range(math.ceil(len(List)/2)):
        ProductsList.append(List[i] * List[N-1-i])

    return "Произведения пар чисел: " + str(ProductsList)
# Задание 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значениями дробных частей элементов.
# *Пример:* [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)
def Task_3_FractionalPartsDifference(N):
    import OwnFunctions as OFs
    import random
    import math 

    N = OFs.input_natural_number("Введите натуральное число - длину списка: ")
    List = [random.randint(0,10001) / 1000 for i in range(0, N)]
    print("Список чисел:", List)
    FractionalPartMin = 1
    FractionalPartMax = 0
    for i in (range(len(List))):
        if (FractionalPartMin > List[i]-math.floor(List[i])):
            FractionalPartMin = round(List[i]-math.floor(List[i]),3)
        elif (FractionalPartMax < List[i]-math.floor(List[i])):
            FractionalPartMax = round(List[i]-math.floor(List[i]),3)

    return "Разница между максимальным (" + str(round(FractionalPartMax,4)) + ") и минимальным (" + str(round(FractionalPartMin,4)) + ") значениями дробных частей элементов составляет: " + str(round(FractionalPartMax-FractionalPartMin,4)) + "."
# Задание 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:* - 45 -> 101101; 3 -> 11; 2 -> 10.
def Task_4_10to2Converstion():
    import random    

    N = random.randint(0,101)
    N10 = N
    N2 = ""
    while N10 > 0 :
        N2 = str(N10%2) + N2
        N10 = N10 // 2

    return "Число " + str(N) + " в двоичной системе счисления: " + str(N2)
# Задание 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:* для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def Task_5_CopleteFibonachi():
    import OwnFunctions as OFs
    
    N = OFs.input_natural_number("Введите натуральное число - длину ряда: ")
    List = [0,1]
    List += [(List := [List[1], List[0] + List[1]]) and List[1] for k in range(N)]
          # Дополнение ряда Фибоначчи отрицательными элементами    
    for i in range(N+1) : 
        List.insert(0, (List[1] - List[0]))

    return "Полный ряд Фибоначчи:" + str(List)

          # Запуск задания 01                 
# print("Сумма чисел на нечетных позициях:", Task_1_OddPositionsSum())
          # Запуск задания 02                 
# print(Task_2_PairsProducts(7))
          # Запуск задания 03                 
# print(Task_3_FractionalPartsDifference(9))
          # Запуск задания 04                 
# print(Task_4_10to2Converstion())
          # Запуск задания 05                 
# print(Task_5_CopleteFibonachi())
'''
'''
          # Домашнее задание к уроку 02
# Задание 01: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 6782 -> 23, 0,56 -> 11.
def DigitsSum (N):
    DigitsList = {'0','1','2','3','4','5','6','7','8','9'}     
    Nstr = str(N)
    DigitsSum = 0
    for i in Nstr: 
        if (i in DigitsList):
            DigitsSum += int(i)
    return "Сумма цифр числа " + format(N, 'f') + " составляет: " + str(DigitsSum)
# Задание 02: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4).
def ProductSets (N):
    import math

    ResultString = ""
    for i in range (1, N) :
         ResultString += str(math.factorial(i)) + ", "
    ResultString += str(math.factorial(N))
    return "Набор произведений от 1 до " + str(N) + ": [" + ResultString + "]"
# Задание 03: Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример: n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]
def NaturalLogarithmBase (n):
    ResultString = ""
    ResultSum = 0
    for i in range (1,n) :
        ResultString += str((1+1/i)**i) + ", "
        ResultSum += (1+1/i)**i
    ResultString += str((1+1/n)**n)
    ResultSum += (1+1/n)**n
    print("Сумма первых " + str(n) + " элементов ряда равна: " + str(ResultSum))
    return "Элементы ряда от 1-го до " + str(n) + "-го: [" + ResultString + "]"
# Задание 04: Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
def ProdactOfSelectedNums (N,FileName):
    Prodact = 1
    RowString = "Список: ["
    with open(FileName,'r') as f:
        SelectedNums = f.read().split('\n')
    for i in range (-N,N-1):
        RowString += str(i) + ", "
    RowString += str(N) + "]"
    print(RowString)
    print("Порядковые номера элементов для умножения (начиная с 0-го): ", SelectedNums)
    for i in range(0,len(SelectedNums)):
                    # Проверка нахождения номера множителя в диапазоне.
        if (int(SelectedNums[i])>=0 and int(SelectedNums[i])<=N*2):
            Prodact *= (-N+int(SelectedNums[i]))
    return "Произведение указанных чисел равно: " + str(Prodact)
# Задание 05: Реализуйте алгоритм перемешивания списка.
def ListMixing(N):
    import random

    SourceList = []
    for i in range (0,N*2+1):
        SourceList.append(-N+i)
    print(SourceList, "- исходный список.")
    for i in range(N*2):
        OldNumber = random.randint(0,N*2)
        NewNumber = random.randint(0,N*2)
                    # Обмен местами для выбранных элементов.
        if OldNumber != NewNumber:
            SourceList[NewNumber],SourceList[OldNumber] = SourceList[OldNumber],SourceList[NewNumber]
    print(SourceList, "- cписок после", N*2, "шагов перемешивания.") 
    return "Список из " + str(N) + " элементов успешно перемешан."
        
          # Запуск задания 01                 
# print(DigitsSum(5.689716))
          # Запуск задания 02                 
# print(ProductSets(7))
          # Запуск задания 03                 
# print(NaturalLogarithmBase(9))
          # Запуск задания 04                 
# print(ProdactOfSelectedNums(7,"HW_task_02_04.txt"))
          # Запуск задания 05                 
print(ListMixing(5))
'''
'''
          # Домашнее задание к уроку 01
# Задание 01: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным. *Пример:* 6 -> да, 7 -> да, 1 -> нет.
def WeekDayMumber (N):
    match N:
        case 1:
            return "Будний день."
        case 2:
            return "Будний день."
        case 3:
            return "Будний день."
        case 4:
            return "Будний день."
        case 5:
            return "Будний день."
        case 6:
            return "Выходной."
        case 7:
            return "Выходной."
        case _:
            return "Задан несуществующий день недели!"
# Задание 02: Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат. ⋁ - "Или", ⋀ - "И", ¬ - "Не".
# Получаем доказательство теоремы де Моргана для 3 переменных обычным перебором.
def deMorgan ():
    print("¬(X ⋁ Y ⋁ Z)        =         ¬X ⋀ ¬Y ⋀ ¬Z")
    for x in 0,1:
        for y in 0,1:
            for z in 0,1: 
#                print(" ",x," ",y," ",z, "->", not(x or y or z), "", (not(x) and not(y) and not(z)),"<-","",x," ",y," ",z)
                print("%3d %3d %3d" % (x,y,z), "->", "%5s" % (not(x or y or z)), "%5s" % (not(x) and not(y) and not(z)),"<-", "%2d %4d %4d" % (x,y,z))
    return "Теорема доказана для 3 переменных."
# Задание 03: Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0,
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:* x=34; y=-30 -> 4; x=2; y=4 -> 1; x=-34; y=-30 -> 3.
def PointLocation (X, Y):
    if X==0 or Y==0:
        return "Точка не принадлежит ни одной из четвертей!"
    if X>0 and Y>0:
        return "Точка находится в 1-й четверти."
    elif X<0 and Y>0:
        return "Точка находится во 2-й четверти."
    elif X<0 and Y<0:
        return "Точка находится в 3-й четверти."
    else:
        return "Точка находится в 4-й четверти."
# Задание 04: Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).
def CoordinateRange (Q):
    match Q:
        case 1:
            return "Диапазон возмодных координат в 1-й четверти: 0<X<∞ и 0>Y<∞."
        case 2:
            return "Диапазон возмодных координат во 2-й четвети: -∞<X<0 и 0>Y<∞."
        case 3:
            return "Диапазон возмодных координат в 3-й четверти: -∞<X<0 и -∞>Y<0."
        case 4:
            return "Диапазон возмодных координат в 4-й четверти: 0<X<∞ и -∞>Y<0."
        case _:
            return "Задана несуществующая четверть!"
# Задание 05: Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# *Пример:* A (3,6); B (2,1) -> 5,09; A (7,-5); B (1,-1) -> 7,21.
def Distance_2D(Ax,Ay,Bx,By):
    return ((Bx-Ax)**2 + (By-Ay)**2)**(1/2)
        
          # Запуск задания 01                 
#print(WeekDayMumber(9))
          # Запуск задания 02                 
# print(deMorgan())
          # Запуск задания 03                 
# print(PointLocation(2,-2))
          # Запуск задания 04                 
# print(CoordinateRange(4))
          # Запуск задания 05                 
# print(Distance_2D(0,0,3,4))
'''