# Вы вводите c клавиатуры число - длина стороны равностороннего треугольника. Выведите высоту, площадь и периметр треугольника. Вывод должен быть вида:
# "Высота треугольника: 12.5
# Площадь треугольника: 24.3
# Периметр треугольника: 18.2"
num = float(input('Сторона равностороннего треугольника равна: '))

H = (num*3**(1/2))/2
S = 1/2*num*H
P = num*3

print(f"Высота треугольника равна: {round(H, 2)}"
      f"\n'Площадь треугольника равна: {round(S, 2)}"
      f"\nПериметр треугольника равен: {round(P, 2)}")
