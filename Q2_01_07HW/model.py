def get_new_phone_number():
    phone_number = input("Введите номер телефона: ")
    name = input("Введите имя абонента: ")
    with open('PhoneList.txt') as f: datafile = f.readlines()
    for line in datafile:
        if (phone_number + ";") in line: return 0
    return (phone_number, name)

def find_phone_number ():
    phone_number = input("Введите номер телефона для поиска: ")
    with open('PhoneList.txt') as f: datafile = f.readlines()
    for line in datafile:
        if (phone_number + ";") in line: return (line.split(';'))
    print("Номер отсутствует в списке.")
    return 0