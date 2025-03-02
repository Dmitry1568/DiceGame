from dice import random_dice

a = input("Если хотите сыграть в игральную кость, то напишите (кубик),или стоп для завершения: ")
while a != 'стоп':
    if a == 'кубик':
        print('Какое число выпадет?(от 1 до 6): ')
        b = int(input())
        print('Значение выпавшего кубика:', random_dice(a))
        if b == random_dice(a):
            print('Вы угадали!')
        else:
            print('Вы не угадали, вам повезёт в следующий раз!')
        break