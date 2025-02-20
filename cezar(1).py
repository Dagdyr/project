from time import perf_counter as time

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            encrypted += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


with open("materials/text.txt", "r", encoding="utf-8") as f:
    data = f.read()


shift_key = 3
start = time()
encrypted_data = caesar_encrypt(data, shift_key) 
decrypted_data = caesar_decrypt(encrypted_data, shift_key)
end = time()
print("Время шифрования и расшифровки сообщения методом Цезаря:", end - start, "секунд")

assert data == decrypted_data, "Ошибка: расшифрованный текст не совпадает с исходным!"
