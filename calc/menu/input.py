from ast import Continue


def input_number():
    while True:
        a = input('Введите первое число: ')
        try:
            return float(a)
        except:
            try:
                return complex(a)
            except:
                print('Не верный ввод, попробуйе снова ')

def input_operation():
    while True:
        print('Введите номер операции: ')
        print('1 - "+"')
        print('2 - "-"')
        print('3 - "*"')
        print('4 - "/"')
        op = input()
        if op not in ['1','2','3','4']:
            print("Error")
            continue
        return op

    


