from Crypto.Cipher import AES
import base64
import logging
from logging.handlers import RotatingFileHandler
import asyncio
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s]%(levelname)s: %(message)s(%(name)s)')

file_handler = RotatingFileHandler("hw4_aes_ecb_decrypted.log", encoding='utf-8', mode='a+')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)  
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def zero_padding(data, block_size = 16):
    return data + b'\x00' * (block_size - len(data) % block_size)

def decrypt_async(ciphertext_base64, key):
    ciphertext = base64.b64decode(ciphertext_base64)    
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        plaintext = cipher.decrypt(ciphertext).rstrip(b'\x00').decode('utf-8')
        logger.error(f'解密成功: {key}, {plaintext}')
        return key
    except:
        pass


ciphertext_base64 = "89NEvN56VtNjo1w5x3whmFUOZOqTaRyoMnIrPjCGKUv5n7kgGFHDmStzEgDFAU7QnZOK9MLeO/FW4etzIOhpKfOsw5xSD4Em72X1O2FRfaM="
for a in range(32, 127):
    start = time.time()
    for b in range(32, 127):
        for c in range(32, 127):
            for d in range(32, 127):
                key = '''2%s?%smYD;@%s;x%sv"i'''%(chr(a), chr(b), chr(c), chr(d))
                key_bytes = key.encode('utf-8')
                decrypt_async(ciphertext_base64, key_bytes)
    end = time.time()
    logger.error('加入解密任務: {}/{}, 預計剩餘時間: {}'.format(a-32+1, 127-32+1, (end-start)*(127-a+1)))