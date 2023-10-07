import numpy as np
import cv2
import random

BLOCK_PIXEL_SIZE = 3
articles_path = './large_articles.txt'
encrypted_articles_path = './large_encrypted_articles.png'

"""Step 1"""
with open(articles_path, 'r', encoding='utf-8') as file:
    file_contents = file.read()
    """Step 2"""
    ascii_text = [ord(char) for char in file_contents]

"""Step 3"""
rgb_values = []
for i in range(0, len(ascii_text), 3):
    subset = ascii_text[i:i+3]
    while len(subset) < 3: 
        subset.append(0)
    rgb_values.append(subset)

"""create key"""


L = len(rgb_values)
#Randomly chosen maximum value of the expected value of the multiplier
RCMVEVM = L ** (1/4) * 2 - 1
N = {
        'x': int(random.uniform(1, RCMVEVM)),
        'y': int(random.uniform(1, RCMVEVM)),
        'a': int(random.uniform(1, RCMVEVM)),
        'b': int(random.uniform(1, RCMVEVM))
    }
product = N['x'] * N['y'] * N['a'] * N['b']

while (product > L):
    selected_variable = random.choice(['x', 'y', 'a', 'b']) 
    N[selected_variable] -= 1
    product = N['x'] * N['y'] * N['a'] * N['b']

while (product < L):
    selected_variable = random.choice(['x', 'y', 'a', 'b']) 
    N[selected_variable] += 1
    product = N['x'] * N['y'] * N['a'] * N['b']

max_len_of_variable = len(str(max(N.values())))
numbers = list(range(1, N['a']*N['b'] + 1))
load_order = ""
random.shuffle(numbers)
load_order = [str(num).zfill(max_len_of_variable) for num in numbers]
load_order_key = ''.join(load_order)

key = "%s,%s,%s,%s,%s"%(N['x'], N['y'], N['a'], N['b'], load_order_key)

"""Step 4"""
image_height = N['y'] * N['b'] * BLOCK_PIXEL_SIZE
image_width = N['x'] * N['a'] * BLOCK_PIXEL_SIZE
image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

for i, chunk_index in enumerate(load_order):
    chunk_x = (i % N['a']) * N['x']
    chunk_y = (i // N['a']) * N['y']
    chunk_colors = list(rgb_values)[i * N['x'] * N['y']:i * N['x'] * N['y'] + N['x'] * N['y']]

    for j, color in enumerate(chunk_colors):
        color_x = (j % N['x']) * BLOCK_PIXEL_SIZE
        color_y = (j // N['x']) * BLOCK_PIXEL_SIZE
        image[chunk_y * BLOCK_PIXEL_SIZE + color_y:chunk_y * BLOCK_PIXEL_SIZE + color_y + BLOCK_PIXEL_SIZE,
              chunk_x * BLOCK_PIXEL_SIZE + color_x:chunk_x * BLOCK_PIXEL_SIZE + color_x + BLOCK_PIXEL_SIZE] = color

cv2.imwrite('encrypted_articles.png', image)
with open('key.txt', 'w', encoding='utf-8') as file:
    file.write(key)