from math import log2


def info():
    var_to_find = input('Что не известно? \n1)N \n2)i \n3)I \n4)K \nНеизвестно: ')
    units_input = input('введите в каких единицах измерения вы хотите ввести ответ 1)Bit 2)Byte 3)KB 4)MB 5)GB ')
    units_output = input('введите в каких единицах измерения вы хотите получить ответ 1)Bit 2)Byte 3)KB 4)MB 5)GB ')
    if var_to_find.strip() == '1':
        i = int(input('Введи i: '))
        i = transfer_into_bits(i, units_input)
        print(f'N={int(transfer_from_bits(2 ** i))}')
    elif var_to_find == '2':
        what_to_use = input('Что вы хотите использовать? \n1)N \n2)I,K \nИспользую: ')
        if what_to_use == '1':
            N = int(input('Введи N: '))
            N = transfer_into_bits(N, units_input)
            print(f'i={int(transfer_from_bits(log2(N)))}')
        elif what_to_use == '2':
            K = int(input('Введите K: '))
            K = transfer_into_bits(K, units_input)
            I = int(input('Введите I: '))
            I = transfer_into_bits(I, units_input)
            print(f'i={int(transfer_from_bits(I / K))}')
    elif var_to_find == '3':
        what_to_use = input('Что вы хотите использовать? \n1)N,K \n2)i,K \nИспользую: ')
        if what_to_use == "1":
            K = int(input('Введите K: '))
            K = transfer_into_bits(K, units_input)
            N = int(input('Введите N: '))
            N = transfer_into_bits(N, units_input)
            i = log2(N)
            print(f'I={int(transfer_from_bits(K * i))}')
        else:
            K = int(input('Введите K: '))
            K = transfer_into_bits(K, units_input)
            i = int(input('Введите i: '))
            i = transfer_into_bits(i, units_input)
            print(f'I={int(transfer_from_bits(K * i))}')
    elif var_to_find == '4':
        what_to_use = input('Что вы хотите использовать? \n1)N,I \n2)i,I \nИспользую: ')
        if what_to_use == '1':
            K = int(input('Введите K: '))
            K = transfer_into_bits(K, units_input)
            I = int(input('Введите I: '))
            I = transfer_into_bits(I, units_input)
            i = log2(K)
            print(f'I={int(transfer_from_bits(I / i))}')
        else:
            i = int(input('Введите i: '))
            i = transfer_into_bits(i, units_input)
            I = int(input('Введите I: '))
            I = transfer_into_bits(I, units_input)
            print(f'K={int(transfer_from_bits(I / i))}')


def image():
    var_to_find = input('Что не известно? \n1)K \n2)b \nНеизвестно: ')
    units_input = input('введите в каких единицах измерения вы хотите ввести ответ 1)Bit 2)Byte 3)KB 4)MB 5)GB ')
    units_output = input('введите в каких единицах измерения вы хотите получить ответ 1)Bit 2)Byte 3)KB 4)MB 5)GB ')

    if var_to_find == '1':
        b = int(input('Введи b: '))
        b = transfer_into_bits(b, units_input)
        print(f'K = {int(transfer_from_bits(2 ** b, units_output))}')
    elif var_to_find == '2':
        K = int(input('Введи K: '))
        K = transfer_into_bits(K, units_input)
        print(f'b = {int(transfer_from_bits(log2(K), units_output))}')


def sound():
    var_to_find = input('Что не известно? \n1)H \n2)ꚍ \n3)I \n4)t \n5)K \nНеизвестно: ')
    units_input = input('введите в каких единицах измерения вы хотите ввести ответ 1)Bit 2)Byte 3)KB 4)MB 5)GB ')
    units_output = input('введите в каких единицах измерения вы хотите получить ответ 1)Bit 2)Byte 3)KB 4)MB 5)GB ')
    if var_to_find == '1':
        t = int(input('Введи ꚍ: '))
        t = transfer_into_bits(t, units_input)
        print(f'H = {int(transfer_from_bits(1 / t))}')
    elif var_to_find == '2':
        H = int(input('Введи H: '))
        print(f't = {int(transfer_from_bits(1 / H))}')
    elif var_to_find == "3":
        H = int(input('Введи H: '))
        H = transfer_into_bits(H, units_input)
        t = int(input('Введи t: '))
        t = transfer_into_bits(t, units_input)
        b = int(input('Введи b'))
        b = transfer_into_bits(b, units_input)
        print(f'I = {int(transfer_from_bits(H * t * b))}')
    elif var_to_find == "4":
        I = int(input('Введи I: '))
        I = transfer_into_bits(I, units_input)
        H = int(input('Введи H: '))
        H = transfer_into_bits(H, units_input)
        b = int(input('Введи b:'))
        b = transfer_into_bits(b, units_input)
        print(f't = {int(transfer_from_bits(I / (H * b)))}')
    elif var_to_find == "5":
        b = int(input('Введи b:'))
        b = transfer_into_bits(b, units_input)
        print(f'K = {int(transfer_from_bits(2 ** b))}')


def transfer_into_bits(var, units):
    if units == '1':
        return var
    elif units == '2':
        return var / 8
    elif units == '3':
        return var / 8 * 1024
    elif units == '4':
        return var / 8 * 1024 ** 2
    elif units == '5':
        return var / 8 * 1024 ** 3


def transfer_from_bits(var, units):
    if units == '1':
        return var
    elif units == '2':
        return var * 8
    elif units == '3':
        return var * 8 * 1024
    elif units == '4':
        return var * 8 * 1024 ** 2
    elif units == '5':
        return var * 8 * 1024 ** 3


def f11():
    type_of_data = input(
        "С каким типом данным хотите работать?\n1)Изображение \n2)Звук \n3)Информация \nЯ хочу работать с: ")

    if type_of_data == "1":
        image()
    elif type_of_data == "2":
        sound()
    elif type_of_data == "3":
        info()


if __name__ == '__main__':
    f11()
