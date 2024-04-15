# Подключение необходимых библиотек
import numpy as np
import matplotlib.pyplot as plt

# Введение необходимых переменных
xi = []
yi = []
xixi = []
xiyi = []
yiyi = []

sumxi = sumyi = sumxixi = sumxiyi = sumyiyi= 0

# Ввод данных в память программы
elements_cnt = int(input('Введите количество вводимых данных: '))
for element in range(elements_cnt):
    xi.append(float(input(f'Введите x{element + 1}: ')))
    yi.append(float(input(f'Введите y{element + 1}: ')))

# Расчёт дополнительных переменных
for element in range(elements_cnt):
    xixi.append(round(xi[element] * xi[element], 2))
    xiyi.append(round(xi[element] * yi[element], 2))
    yiyi.append(round(yi[element] * yi[element], 2))

# Расчёт значений сумм всех переменных
sumxi = sum(xi)
sumyi = sum(yi)
sumxixi = sum(xixi)
sumxiyi = sum(xiyi)
sumyiyi = sum(yiyi)

# решим систему уравнений
# Создаем матрицу коэффициентов и вектор свободных членов
A = np.array([[sumxi, elements_cnt], [sumxixi, sumxi]])
b = np.array([sumyi, sumxiyi])

# Решаем систему уравнений
x = np.linalg.solve(A, b)

# Выводим промежуточный результат
print('Следовательно, зависимость будет выражаться следующим уравнением: ')
print(f'вектор yx = {x[0]:.2f}x + {x[1]:.2f}')

# Вычисляем коэффициент корреляции
qx = np.sqrt(sumxixi / elements_cnt - (sumxi / elements_cnt) ** 2)
qy = np.sqrt(sumyiyi / elements_cnt - (sumyi / elements_cnt) ** 2)

r = (sumxiyi / elements_cnt - (sumxi / elements_cnt) * (sumyi / elements_cnt)) / (qx * qy)

# Выводим коэффициент корреляции
print(f'Коэффициент корреляции: {r:.2f}')

# Прописываем часть с построением графика
qus_ = str(input("Будете ли вы строить какой-либо график? [Y/N]"))
while True:
    if qus_ == 'Y':
        plt.bar(xi, yi, label='y')
        break          
    elif qus_ == 'N':
        break
    else:
        qus_ = str(input("Введите Y или N: "))