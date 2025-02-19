# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

import math

def compute_statistics(numbers):

    if len(numbers) != 5:
     return "Please provide exactly five numbers."

    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    range_ = maximum - minimum

    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)

    return {
     "Total": total,
     "Average": average,
     "Minimum": minimum,
     "Maximum": maximum,
     "Range": range_,
     "Standard Deviation": std_deviation
    }

numbers = [5, 10, 15, 20, 25]
statistics = compute_statistics(numbers)

for stat, value in statistics.items():
    print(f"{stat}: {value}")

