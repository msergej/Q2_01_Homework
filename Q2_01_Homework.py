import os
os.system('cls||clear')

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