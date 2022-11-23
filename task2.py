# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех
#  значений предикат. ⋀ - and ⋁ - or ¬ - not

x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))

predicate = not ( x or y or z )
result = not x and not y and not z

if predicate == result:

    print('Утверждение истинно!')

else:

    print('Утверждение ложно!')