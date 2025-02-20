from time import perf_counter as time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# Генерируем пару ключей RSA (2048 бит).
key = RSA.generate(2048)
public_key = key.publickey()


# Создаем объекты шифрования и дешифрования с использованием схемы PKCS1_OAEP.
cipher_rsa_enc = PKCS1_OAEP.new(public_key)
cipher_rsa_dec = PKCS1_OAEP.new(key)

# Читаем тестовый файл малого размера, так как RSA неэффективен для больших объемов данных.
with open("materials/small_text.txt", "r", encoding="utf-8") as f:
    data = f.read() 
data_bytes = data.encode('utf-8')

start = time()
encrypted_data = cipher_rsa_enc.encrypt(data_bytes) 
 
decrypted_data = cipher_rsa_dec.decrypt(encrypted_data)
end = time()

print("Время шифрования и расшифровки сообщения методом RSA:", end - start, "секунд")
assert data_bytes == decrypted_data, "Ошибка: расшифрованный текст не совпадает с исходным!"
