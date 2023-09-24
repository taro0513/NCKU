import cv2

BLOCK_PIXEL_SIZE = 1

encrypted_articles_path = './large_encrypted_articles.png'

"""Step 1"""
image = cv2.imread(encrypted_articles_path)

height, width, _ = image.shape

rgb_values = []

"""Step 2 & 3"""
for y in range(0, height, BLOCK_PIXEL_SIZE):
    for x in range(0, width, BLOCK_PIXEL_SIZE):
        grid = image[y:y+BLOCK_PIXEL_SIZE, x:x+BLOCK_PIXEL_SIZE]
        rgb = (int(grid[:, :, 0].mean()), 
               int(grid[:, :, 1].mean()), 
               int(grid[:, :, 2].mean()))
        rgb_values.append(rgb)

"""Step 4"""
decrypted_articles = "".join(
    [chr(rgb[0]) + chr(rgb[1]) + chr(rgb[2]) for rgb in rgb_values]
    )

"""Step 5"""
with open('large_decrypted_articles.txt', 'w', encoding='utf-8') as file:
    file.write(decrypted_articles)
