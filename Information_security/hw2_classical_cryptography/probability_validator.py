import random
import time

num_trials = 100000
# total_error = 0
total_time = 0
for _ in range(num_trials):
    s = time.time()
    L = random.randint(100000, 10000000)
    L_most_likely_base = L ** (1/4) * 2 -1
    N = {
        'a': random.uniform(1, L_most_likely_base),
        'b': random.uniform(1, L_most_likely_base),
        'c': random.uniform(1, L_most_likely_base),
        'd': random.uniform(1, L_most_likely_base)
    }
    product = N['a'] * N['b'] * N['c'] * N['d']
    while (product < L):
        selected_variable = random.choice(['a', 'b', 'c', 'd']) 
        N[selected_variable] += 1
        product = N['a'] * N['b'] * N['c'] * N['d']
        # print(N['a'], N['b'], N['c'], N['d'], product)
    e = time.time()
    total_time += e - s
        
average_time = total_time / num_trials

#3.0150020122528075e-05
print(f"平均時間為：{average_time}")
