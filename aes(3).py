from time import perf_counter as time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    # добавляем отступ, чтобы длина строки стала кратна 16 байтам.
    padding_length = 16 - (len(data) % 16)
    return data + (chr(padding_length) * padding_length)

def unpad(data):
    # Извлекаем последний символ, определяющий длину отступа, и удаляем его.
    padding_length = ord(data[-1])
    return data[:-padding_length]


with open("materials/text.txt", "r", encoding="utf-8") as f:
    data = f.read()
# Приводим текст к формату, пригодному для шифрования: добавляем отступы и кодируем в байты.
data_bytes = pad(data).encode('utf-8')

# Генерируем случайный 128-битный ключ и IV (начальный вектор) по 16 байт.
key = get_random_bytes(16)
iv = get_random_bytes(16)

# Создаем объект шифрования AES в режиме CBC.
cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
start = time() 
encrypted_data = cipher_encrypt.encrypt(data_bytes) 

# Для расшифрования создаем новый объект с теми же ключом и IV.
cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)

decrypted_data = cipher_decrypt.decrypt(encrypted_data)
end = time()

# Преобразуем байты обратно в строку и удаляем добавленные отступы.
decrypted_text = unpad(decrypted_data.decode('utf-8'))
print("Время шифрования и расшифровки сообщения методом AES:", end - start, "секунд")
assert data == decrypted_text, "Ошибка: расшифрованный текст не совпадает с исходным!"
