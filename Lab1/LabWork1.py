import math

# Константы для перевода величин друг в друга
JTF = 3  # В одном ярде три фута
MHTFS = 5280  # В одном ярде три фута

# Ввод данных для расчета
# d1 = int(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды)"))
d1 = 8
# d2 = int(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы)"))
d2 = 10
# h = int(input("Введите боковое смещение между спасателем и утопающим, h (ярды)"))
h = 50
# v_sand = int(input("Введите скорость движения спасателя по песку, v_sand (мили в час)"))
vSand = 5
# n = int(input("Введите коэффициент замедления спасателя при движении в воде, n"))
n = 2
# θ = float(input("Введите направление движения спасателя по песку, θ (градусы)"))
θ = 39.413

# ВЫЧИСЛЕНИЯ
# Тангенс угла направления движения - Tgθ
Tgθ = math.tan(math.pi * θ / 180)
# print(Tgθ)
# Величина вертикального смещения до границы раздела сред - x, (футы)
x = d1 * JTF * Tgθ
# print(x)
# Величина диагонального смещения до границы раздела сред (по песку) - L1, (футы)
L1 = ((d1 * JTF) ** 2 + x ** 2) ** 0.5
# print(L1)
# Величина диагонального смещения от границы раздела сред (по воде) - L2, (футы)
L2 = ((h * JTF - x) ** 2 + d2 ** 2) ** 0.5
# print(L2)
# Перевод скорости из миль в час в футы в секунду - v_f_sand
vFsand = vSand * 5280 / (60 * 60)
# print(v_f_sand)

# Определение необходимого времени t, (секунды) c округлением до одного знака
time = round(1 / vFsand * (L1 + n * L2), 1)

print("")  # пробел
print("Если спасатель начнёт движение под углом θ =", θ, "градусов, он достигнет утопащего через", time, "секунд.")