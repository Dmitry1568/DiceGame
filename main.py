from dice import random_dice

user_input = input("Если хотите сыграть в игральную кость, то напишите (кубик), или стоп для завершения: ")
while user_input != 'стоп':
    if user_input == 'кубик':
        print('Какое число выпадет? (от 1 до 6): ')
        user_guess = int(input())
        dice_result = random_dice()
        print('Значение выпавшего кубика:', dice_result)
        if user_guess == dice_result:
            print('Вы угадали!')
        else:
            print('Вы не угадали, вам повезёт в следующий раз!')
    user_input = input("Если хотите сыграть ещё раз, напишите (кубик), или стоп для завершения: ")