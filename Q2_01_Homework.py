import os
os.system('cls||clear')

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