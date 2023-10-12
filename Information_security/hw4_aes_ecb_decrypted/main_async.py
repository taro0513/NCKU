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
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def zero_padding(data, block_size = 16):
    return data + b'\x00' * (block_size - len(data) % block_size)

async def decrypt_async(ciphertext_base64, key):
    ciphertext = base64.b64decode(ciphertext_base64)    
    cipher = AES.new(key, AES.MODE_ECB)
    try:
        plaintext = cipher.decrypt(ciphertext).rstrip(b'\x00').decode('utf-8')
        logger.info(f'解密成功: {key}, {plaintext}')
        return key
    except UnicodeDecodeError as e:
        error = f'解密失敗: {key}, {e}'
        logger.info(error)
    except Exception as e:
        error = f'解密失敗: {key}, {e}'
        logger.error(error)

async def main():
    tasks = []
    ciphertext_base64 = "89NEvN56VtNjo1w5x3whmFUOZOqTaRyoMnIrPjCGKUv5n7kgGFHDmStzEgDFAU7QnZOK9MLeO/FW4etzIOhpKfOsw5xSD4Em72X1O2FRfaM="
    for a in range(32, 127):
        start = time.time()
        for b in range(32, 127):
            for c in range(32, 127):
                for d in range(32, 127):
                    key = '''2%s?%smYD;@%s;x%sv"i'''%(chr(a), chr(b), chr(c), chr(d))
                    key_bytes = key.encode('utf-8')
                    task = asyncio.ensure_future(decrypt_async(ciphertext_base64, key_bytes))
                    tasks.append(task)
                    # logger.info(f'加入解密任務: {key}')
        end = time.time()
        logger.info('加入解密任務: {}/{}, 預計剩餘時間: {}'.format(a-32+1, 127-32+1, (end-start)*(127-a+1)))
    results = await asyncio.gather(*tasks)
    
    for result in results:
        if result:
            logger.info(f'解密成功: {key}')
            
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())