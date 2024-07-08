import random

def generate_zero_sum_array(n):
    array = [random.randint(0, n-1) for _ in range(n-1)]
    total_sum = sum(array)
    array.append(-total_sum)
    return array

n = 5
result = generate_zero_sum_array(n)
print(result)