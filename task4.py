# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int (input ('Введите номер четверти: '))

if a <= 0 or a > 4:

    print('Такой четверти не существует!')

elif a == 1:

    print('х(0; +∞) и у(0; +∞)')

elif a == 2:

    print('х(0; -∞) и у(0; +∞)')

elif a == 3:

    print('х(0; -∞) и у(0; -∞)')

else:

    print('х(0; +∞) и у(0; -∞)')