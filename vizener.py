from time import perf_counter as time

def vigenere_encrypt(text, key):
    encrypted = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    for i, char in enumerate(text):
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shift = (ord(char) - base + (key_as_int[i % key_length] - base)) % 26
            encrypted.append(chr(shift + base))
        else:
            encrypted.append(char)
    return "".join(encrypted)

def vigenere_decrypt(cipher_text, key):
    decrypted = []
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            base = 65 if char.isupper() else 97
            shift = (ord(char) - base - (key_as_int[i % key_length] - base)) % 26
            decrypted.append(chr(shift + base))
        else:
            decrypted.append(char)
    return "".join(decrypted)


with open("materials/text.txt", "r", encoding="utf-8") as f:
    data = f.read()

key = "SECRET"  

start = time()
encrypted_data = vigenere_encrypt(data, key) 

decrypted_data = vigenere_decrypt(encrypted_data, key)
end = time()

print("Время шифрования и расшифровки сообщения методом Виженера:", end - start, "секунд")
assert data == decrypted_data, "Ошибка: расшифрованный текст не совпадает с исходным!"
