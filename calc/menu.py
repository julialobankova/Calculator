from calculations import calculation
from log import read_log

def menu ():
    flag = True
    while flag:
        print("1 - Сделать расчет")
        while True:
            print('2 - Показать Лог')
            print('3 - Выход')   
            choice = input()
            if choice not in['1', '2', '3']:
                print('Error')
                continue
            if choice == '1':
                calculation()
                break
            if choice == '2':
                read_log()
                break
            else:
                flag = False
                break
            
if __name__  == '__main__':
    menu()     
