# PracticalWork3.
# Работа с модулями стандартной библиотеки

import math
import random
import statistics

nums = [random.randint(0, 100) for i in range(10)]
print(*nums)

# подсчет суммы чисел списка,
sumNums = math.fsum(nums)

# подсчет среднего значения,
mediumNums = statistics.mean(nums)

# подсчет медианы (median)
medianNums = statistics.median(nums)

# подсчет стандартного отклонения (stdev),
devNums = statistics.stdev(nums)

print(sumNums)
print(mediumNums)
print(medianNums)
print("{:.2f}".format(devNums))
