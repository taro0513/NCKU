import numpy as np
import cv2

BLOCK_PIXEL_SIZE = 1
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

"""Step 4"""
num_blocks = len(rgb_values)
block_size = int(np.sqrt(num_blocks)) +1 
image_size = block_size * BLOCK_PIXEL_SIZE
image = np.zeros((image_size, image_size, 3), dtype=np.uint8)

"""Step 5 & 6"""
for i, rgb in enumerate(rgb_values):
    row = i // block_size
    col = i % block_size
    x1 = col * (image_size // block_size)
    y1 = row * (image_size // block_size)
    x2 = (col + 1) * (image_size // block_size)
    y2 = (row + 1) * (image_size // block_size)
    image[y1:y2, x1:x2] = rgb

"""Step 7"""
cv2.imwrite(encrypted_articles_path, image)
